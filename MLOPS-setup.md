# MLOPS

## Setting up mlops from scratch 

1. create a repo<repo-name> and clone it locally 
2. create a conda env in your repo ```python 
3. conda create --name env_name python=3.11```
4. create a python script `template.py` your repo's root folder and add the below code in that 
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
3. Now create the `requirement.txt` file and the package required for project and some default and nessaccary are written below 
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

4. `-e .` will search for the `setup.py` and it will automatically setup the env by localizing the packages and adding some information about your project to make it look more professional. Write below code in `setup.py`
```python

```