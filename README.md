# Boolm-s-Level-Detection-A-MLOPS-Project


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
