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

#### 11. Check location to store Prefect Artifacts 
```bash
prefect storage ls
```

#### 12. Create location to store Prefect Artifacts 
```bash
prefect storage create
```

#### 13. Create the deployment schedule
```bash
prefect deployment create <python code.py>
```

#### 14. Create the deployment schedule
```bash
prefect deployment create <python code.py>
```
If succesful, future runs will be visible as below: 

<img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/scheduled-runs.png" width="700" height="400">

#### 15. Create a work queue using the Prefect Interface and save the unique id generated

#### 16. View a list of existing work queues
```bash
prefect work-queue ls
```

#### 17. View future schedules of an existing work queue
```bash
prefect work-queue preview <unique code of the work queue>
```

## Running Prefect remotely on AWS 

 - Login to AWS Console and create an EC2 instance
 - A basic t2-micro instance will be sufficient.
 - Ensure the security groups assigned to the EC2 instance has below mentioned inbound rules:
 
 <img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/ec2-security-group.png" width="700"
     height="300">
 
 - Change current directory to .ssh directory
     - ```cd /Users/txxxxxxxxxxxxj/.ssh```

 - Connect/SSH to the EC2 instance
     - ```ssh -i "key-name.pem" ec2-user@ec2-99-999-99-999.eu-west-2.compute.amazonaws.com```
 
 - Install Pip (for Linux Only)
     - ```sudo yum -y install python-pip```
    
 - Install Conda
     - ```wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh```
     - ```sh Anaconda3-2020.02-Linux-x86_64.sh```
     - ```source ~/.bashrc```     
 
 - Create & Activate Conda environment
     -```conda create --name <environment name> python=3.9``` 
     -```conda activate <environment name> 
 
 - Install Prefect
          - ```pip install prefect==2.0b5```
     
  - Configure Prefect (Run on Local)  
     - ```prefect config set PREFECT_ORION_UI_API_URL="http://<ec2 public ip address>:4200/api"```

  - View Prefect Configuration (Run on Local) 
     - ```prefect config view```

  - Command to Change Prefect Configuration (Run on Local) 
     - ```prefect config unset <variable name>``` e.g. <PREFECT_ORION_UI_API_URL>   
   
  - Start Orion Server (Run on VM) 
     - ```prefect orion start --host 0.0.0.0``` 
     - If successful, Orion server UI will be served as below:
     <img src="https://github.com/tanmaybhardwaj/mlops-zoomcamp/blob/main/03-Orchestration%20and%20ML%20Pipelines/images/orion%20server%20aws.png"
          width="700" height="300">
          
  - From the local machine\terminal, configure to access the API
     - ```prefect config set PREFECT_API_URL="http://<ec2 public ip address>:4200/api"```

  - From the local system, run python code homework.py 
     - ```bash python homework.py```
    
         If successful, MSE values of training and validations sets will be printed on command line and succesful workflow will be visible in the Prefect          Interface hosted on the AWS.
 
