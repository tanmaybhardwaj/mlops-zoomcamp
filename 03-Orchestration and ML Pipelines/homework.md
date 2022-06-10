### Solution to Homework of Module #3

#### Q1. Converting the script to a Prefect flow
We want to bring this to workflow orchestration to add observability around it. The main function will be converted to a flow and the other functions will be tasks. After adding all of the decorators, there is actually one task that you will need to call .result() for inside the flow to get it to work. Which task is this?

- read_data
- prepare_features
- train_model
- run_model

#### Answer: train_model (please follow homework.py file for code details)


#### Q2. Parameterizing the flow
What is the validation MSE when running the flow for ```main(date="2021-08-15")```?
#### Answer : 11.637

<img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/question-02-results.png" width="900" height="300">

#### Q3. Saving the model and artifacts

What is the file size of the DictVectorizer that we trained when the date is 2021-08-15?

- 13,000 bytes
- 23,000 bytes
- 33,000 bytes
- 43,000 bytes

#### Answer: 13,000 bytes

#### Q4. Creating a deployment with a CronSchedule

What is the Cron expression to run a flow at 9 AM every 15th of the month?

- ```* * 15 9 0```
- ```9 15 * * *```
- ```0 9 15 * *```
- ```0 15 9 1 *```

#### Answer: ```0 9 15 * *```

#### Q5. Viewing the Deployment

How many flow runs are scheduled by Prefect in advance? You should not be counting manually. There is a number of upcoming runs on the top right of the dashboard.

- 0
- 3
- 10
- 25

#### Answer: 15
