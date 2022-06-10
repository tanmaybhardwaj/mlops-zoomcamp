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

#### 4. Create a folder/directory named 'data'
```bash
mkdir data
```

#### 5. Download below mentioned parquet files from the URL and save them to data folder
```bash
URL = https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
File 1 = January 2021 For-Hire Vehicle Trip Records (PARQUET)
File 2 = February 2021 For-Hire Vehicle Trip Records (PARQUET)
```
