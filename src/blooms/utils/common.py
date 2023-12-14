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
    return f"~ {size_in_kb} KB"
