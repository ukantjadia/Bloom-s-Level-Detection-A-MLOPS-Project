from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    unzip_dir: Path
    local_data_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    STATUS_FILE: str
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    clean_data_path: Path
    augmented_data_path: Path
    new_data_path: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    target_columns: str
    training_columns: str
    pipeline_ele_1: str
    pipeline_ele_2: str
    pipeline_ele_3: str
    elastic_model_name: str
    multinomial_model_name: str
    word2vector_model_name: str
    distilBERT_model_name: str
