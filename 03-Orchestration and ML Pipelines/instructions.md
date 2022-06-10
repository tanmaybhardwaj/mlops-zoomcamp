## Follow below instructions to successfully replicate the workflow

#### 1. Create a virtual environment
```bash
conda create --name <environment name> python=3.9
```

#### 2. Activate the virtual environment
```bash
conda activate <environment name>
```

#### 3. Install Prefect 
```bash
pip install prefect==2.0b5
```

#### 4. Install remaining packages as listed in requirements.txt file
```bash
pip install -r requirements.txt
```

#### 5. Create a folder/directory named 'data'
```bash
mkdir data
```

#### 6. Download below mentioned parquet files from the URL and save them to data folder
```bash
URL = https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
File 1 = January 2021 For-Hire Vehicle Trip Records (PARQUET)
File 2 = February 2021 For-Hire Vehicle Trip Records (PARQUET)
```

#### 7. Run python code homework_raw.py
```bash
python homework_raw.py
```
If the setup is correct, the code will print MSE values of training and validations sets.

#### 8. Create a copy of homework_raw.py file and name it homework.py. 
In this new code we will add logic for workflow orchestration. The ```main``` function will be converted to a ```flow``` and 
other functions will be converted to ```tasks```.


#### 9. From a separate terminal/command line start the prefect server
```bash
prefect orion start
```
If successful the server user interface will be served at http://127.0.0.1:4200/

<img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/orion%20server%20startup.png" width="700" height="300">

#### 10. Run python code homework.py 
```bash
python homework.py
```
If successful, MSE values of training and validations sets will be printed on command line and succesful workflow will be visible in the Prefect Interface.

<img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/successful%20flow-01%20.png" width="700" height="300">

<img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/successful%20flow-02.png" width="700"
     height="300">
