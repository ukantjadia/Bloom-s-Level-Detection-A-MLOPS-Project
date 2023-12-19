from blooms.constants import *
from blooms.utils.common import read_yaml, create_directories
from blooms.entity.config_entity import (DataIngestionConfig,DataValidationConfig)


class ConfigurationManager:
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
        config = self.config.data_ingestion  ## fetching the ele from config.yaml

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            unzip_dir=config.unzip_dir,
            local_data_path=config.local_data_path,
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            STATUS_FILE=config.STATUS_FILE,
            root_dir=config.root_dir,
            unzip_data_path=config.unzip_data_path,
            all_schema=schema,
        )
        return data_validation_config
