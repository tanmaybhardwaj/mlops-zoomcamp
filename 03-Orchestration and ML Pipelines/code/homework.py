import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from datetime import datetime
from dateutil.relativedelta import relativedelta
from prefect import flow, task, get_run_logger 
from prefect.task_runners import SequentialTaskRunner


@task
def read_data(path):
    df = pd.read_parquet(path)
    return df

@task
def prepare_features(df, categorical, train=True):
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    mean_duration = df.duration.mean()

    if train:
        print(f"The mean duration of training is {mean_duration}")
    else:
        print(f"The mean duration of validation is {mean_duration}")

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    return df
    
@task
def train_model(df, categorical):
    train_dicts = df[categorical].to_dict(orient='records')
    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dicts) 
    y_train = df.duration.values

    print(f"The shape of X_train is {X_train.shape}")
    print(f"The DictVectorizer has {len(dv.feature_names_)} features")

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_train)
    mse = mean_squared_error(y_train, y_pred, squared=False)
    print(f"The MSE of training is: {mse}")
    return lr, dv


@task
def run_model(df, categorical, dv, lr):
    val_dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(val_dicts) 
    y_pred = lr.predict(X_val)
    y_val = df.duration.values

    mse = mean_squared_error(y_val, y_pred, squared=False)
    print(f"The MSE of validation is: {mse}")
    return


def get_paths(date):
    #check date format
    format = "%Y-%m-%d"
    if date != None:
        try:
            file_date=datetime.strptime(date, format)
            training_date = file_date - relativedelta(months=2)
            training_file_path = './data/fhv_tripdata_'+str(training_date.year)+'-'+(str(training_date.month).zfill(2))+'.parquet'
            validation_date = file_date - relativedelta(months=1)
            validation_file_path = './data/fhv_tripdata_'+str(validation_date.year)+'-'+(str(validation_date.month).zfill(2))+'.parquet'
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
    else:
        file_date = datetime.today()
        training_date = file_date - relativedelta(months=2)
        training_file_path = './data/fhv_tripdata_'+str(training_date.year)+'-'+(str(training_date.month).zfill(2))+'.parquet'
        validation_date = file_date - relativedelta(months=1)
        validation_file_path = './data/fhv_tripdata_'+str(validation_date.year)+'-'+(str(validation_date.month).zfill(2))+'.parquet'

    return(training_file_path,validation_file_path)


@flow(task_runner=SequentialTaskRunner())
def main(date="2021-08-15"):
#def main(train_path: str = './data/fhv_tripdata_2021-01.parquet', 
#           val_path: str = './data/fhv_tripdata_2021-02.parquet'):

    train_path, val_path = get_paths(date)
    categorical = ['PUlocationID', 'DOlocationID']

    df_train = read_data(train_path)
    df_train_processed = prepare_features(df_train, categorical)

    df_val = read_data(val_path)
    df_val_processed = prepare_features(df_val, categorical, False)

    # train the model
    lr, dv = train_model(df_train_processed, categorical).result()
    run_model(df_val_processed, categorical, dv, lr)

#main()

from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runners import SubprocessFlowRunner

DeploymentSpec(
    name="model_training",
    flow=main,
    flow_runner=SubprocessFlowRunner(),
    schedule=CronSchedule(
        cron="0 9 15 * *",
        timezone="Europe/London"),
)