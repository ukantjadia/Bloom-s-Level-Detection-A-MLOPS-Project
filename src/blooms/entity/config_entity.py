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
