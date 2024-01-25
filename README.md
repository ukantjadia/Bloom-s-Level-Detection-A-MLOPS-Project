# Boolm-s-Level-Detection-A-MLOPS-Project


---
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in the src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py 
---

## Walkthrough of my MLOPS-Project 

### Environment setup

Follow my MLOPS setup method and do the setup till the `/src/project-name/common.py`

Now I am following the steps of the MLOPS project as mentioned in the method

### Data Ingestion 

In this, step we will access our data and make it accessible for future use

**Step 1:** set up the `config/config.yaml` file by defining some default variables like root_dir,data_url,data_path,path_zip_data etc.

**Step 2:**

**Step 3:**

**Step 4:** Now create a new notebook in research dir as `research/01_data_ingesion.ipynb`, 
Now open it and make sure your dir is the root folder of your project 


Now follow the Sklaton structure for working further with the notebook


Sklaton of notebook

- Define class `StageNameConfig`  

---


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlops python=3.10.13 -y
```

```bash
conda activate mlops
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
### STEP 03- set some python env variable for tracking  

**In conda env**

```python 

# to set new variable 
conda env config vars set MY_VARIABLE=my_value 

# to access that variable 
os.environ.get('MY_VARIABLE')

# to see all available variables 
conda env config vars list

```
**In normal python env**

```python 
# to set new variable
set MY_VARIABLE=my_value

# to access that variable 
os.environ.get('MY_VARIABLE')

```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub.com
<!-- [dagshub](https://dagshub.com/) -->

```cmd
MLFLOW_TRACKING_URI=https://dagshub.com/ukantjadia/Boolm-s-Level-Detection-A-MLOPS-Project.mlflow \
MLFLOW_TRACKING_USERNAME=ukantjadia \
MLFLOW_TRACKING_PASSWORD=xxxxxxxxxxxxxx \
python script.py
```

Run this to export as env variables:


```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ukantjadia/Boolm-s-Level-Detection-A-MLOPS-Project.mlflow

export MLFLOW_TRACKING_USERNAME=ukantjadia 

export MLFLOW_TRACKING_PASSWORD=xxxxxxxxxxxxxx

```
