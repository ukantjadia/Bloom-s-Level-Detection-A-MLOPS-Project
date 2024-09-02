# MLOPS

## Setting up mlops from scratch 

1. create a repo<repo-name> and clone it locally 
2. create a conda env in your repo 
`conda create --name env_name python=3.11` Create a Python script `template.py` in your repo's root folder and add the below code to that 
```python 
import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

### Add your project name below
project_name = "projectName"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
```

3. Now open the `requirement.txt` file and the package required for the project or some defaults and necessary are written below 
```text 
pandas
mlflow
notebook
numpy
scikit-learn
matplotlib
python-box
pyYAML
tqdm
ensure
joblib
types-pyYAML
Flask
Flask-Cors
-e .
```

4. `-e .` will search for the `setup.py` and it will automatically set up the env by localizing the packages and adding some information about your project to make it look more professional. Write the below code in `setup.py`
```python
import setuptools 

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Repo-Name"
AUTHOR_USER_NAME = "github_username"
SRC_REPO = "source_folder_name"
AUTHORE_EMAIL = "username@gmail.ocom"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHORE_EMAIL,
    description = "A small project to demonstarte MLOPS",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
```


5. Now create the python logging(info level) util for handling and recognizing the issues after development. So write the below code in `src/project-name/__init__.py` of your source folder 
```python 
import os
import sys
import logging
import colorlog

# Define a color formatter
formatter = colorlog.ColoredFormatter(
    "[%(asctime)s: %(log_color)s%(levelname)s%(reset)s: %(module)s: %(message)s]",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Set up the logger with color formatter
logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
    ]
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger = logging.getLogger("mlops-project")
logger.addHandler(console_handler)
```

6. Now check the logging function by adding the below sample code in the `main.py`. You will see the output in the terminal with your message
```python
from foodImgClassification import logger

logger.info('Welcome to our custom logging') # your sample logging message
```

7. Now add some common functions in the source utils folder so we can use them whenever we want without defining each time. Write the below code in `src/project-name/utils/common.py`
```python 
from pathlib import Path
from box import ConfigBox
from blooms import logger
from ensure import ensure_annotations
from typing import Any
from box.exceptions import BoxValueError
import yaml
import json
import os
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succcessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empy")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as file:
        content = json.load(file)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"Size: {size_in_kb} file: {path}")
    return size_in_kb
```

7. Now follow the below-given steps for every stage of machine learning recursively
    
    7.0 Add the constant in your `project_name/src/constants/__init__.py`
    7.1 Steps to follow
    1. Update config.yaml
    2. Update schema.yaml
    3. Update params.yaml
    4. Update the entity
    5. Update the configuration manager in the src config
    6. Update the components
    7. Update the pipeline 
    8. Update the main.py
    9. Update the app.py 

> **Machine learning steps**
> 
> Data Ingestion: collecting the data and setting up for further use 
> 
> Data Validation: Checking the data type, format, and other condition to see the validaty and usability of the data
> 
> Data Transformation: Doing the preprocessing and spliting the test and train data set
> 
> Model Training: Selecting the sutaible mahcine learning algorithm and creating a model by training
> 
> Model Evaluation: Testing on the data and verifying with the measurement/result matrices
> 
> Model Prediction: Doing the prediction with user input

### Adding constant in `project_name/src/constants/__init__.py`
1. We need to add some paths as constant for our project 
```python
from pathlib import Path
CONFIG_FILE_PATH = Path('config/config.yaml')
PARAMS_FILE_PATH = Path('params.yaml')
SCHEMA_FILE_PATH = Path('schema.yaml')
```

## Following step 7.1 in detail

### 7.1.1 Update config yaml in detail
1. Start by adding the path of your artifacts dir as `artifacts_root: artifacts`  in `config/config.yaml`.
2. Now add the first step **Data Ingestion** from Machine learning steps in `config.yaml` with some required information like data path, data source URL, path of root dir for data ingestion, 
```yaml
data_ingestion:
    root_dir: artifacts/data_ingestion
    source_URL: "https://example.zip"
    local_data_path: artifacts/data_ingestion/data.zip
    unzip_dir: artifacts/data_ingestion/
```  

### 7.1.2 Update schema in detail
1. This is the schema of data which we are going to use for validation 

We will need this to validate our data in a *Data Validation* step 

### 7.1.3 Update params in detail
1. These are the parameters we are going to use in our algorithm

We will need this during the *Model Training* step

### 7.1.4 Update the entity in detail
1. Here we will create a basic class that is working as a bridge between our `config.yaml` file and source code. This class contains all the elements of the current *Machine Learning Step* corresponding to its data type.
```python
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_path: Path
    unzip_dir: Path
```

### 7.1.5 Update the configuration manager in the src config in detail
1. Now we are going to read our data from the yaml files by creating a function with a return type of our entity which we created
```python
from projectSrc.constant import *
from projectSrc.utils.common import read_yaml, create_directories

class configurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
    
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_path=config.local_data_path,
            source_URL=config.source_URL,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
```

### 7.1.6 Update the component 
1. After reading the all required information we will do the required tasks as collecting/downloading and extracting the data
```python
from projectSrc import logger
from projectSrc.utils.common import get_size

import urllib.request as request
import zipfile

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def dowload_data_file(self):
        if not os.path.exists(self.config.local_data_path):
            filename, headers = request.urlretrieve(
                filename=self.config.local_data_path,
                url=self.config.source_URL,
            )
            logger.info(f"{filename} Downloaded! with the following info {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_path))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"{unzip_path} extracted !!")           
```

### 7.1.7 Update the Pipeline 
1. Now we have initialized all the compulsory steps for working or extending our code with minimal and maintainable changes 
2. And now we will connect our all prior steps by creating a pipeline
```pyhon
try: 
    config = configurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.dowload_data_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e
```
