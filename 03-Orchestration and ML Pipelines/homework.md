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
