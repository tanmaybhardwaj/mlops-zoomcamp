 ## 2.0 Experiment Tracking

### 2.1 Experiment tracking intro

### 2.2 Getting started with MLflow

### 2.3 Experiment tracking with MLflow 

### 2.4 Model management 

### 2.5 Model registry 

### 2.6 MLflow in practice 

### 2.7 Homework 

 #### Q1.Install MLflow 
 What's the version that you have?
     
 Answer : 1.26.0 
 
<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/mlflow_version.png" width="800" height="300">

#### Q2.Download and preprocess the data 
  How many files were saved to `OUTPUT_FOLDER` ?
     
  Answer : 4
  
<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/number_of_files.png" width="200" height="200"> 

#### Q3.Train a model with autolog 
  How many parameters are automatically logged by MLflow?
    
  Answer : 17 
  
<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/number_of_parameters.png" width="800" height="400">

## Q4. Launch the tracking server locally
In addition to `backend-store-uri`, what else do you need to pass to properly configure the server?

Answer : `default-artifact-root`

<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/artifact_location.png" width="600" height="200">

## Q5. Tune the hyperparameters of the model
What's the best validation RMSE that you got?

Answer 6.628

<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/best_validation_rmse.png" width="700" height="400">

## Q6. Promote the best model to the model registry

What is the test RMSE of the best model?

Answer 6.55
  
<img src="https://raw.githubusercontent.com/tanmaybhardwaj/mlops-zoomcamp/main/02-experiment-tracking/images/best_test_rmse.png" width="700" height="300">

