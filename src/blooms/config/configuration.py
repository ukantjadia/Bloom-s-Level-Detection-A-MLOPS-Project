from blooms.constants import *
from blooms.utils.common import read_yaml, create_directories
from blooms.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig,
)


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

    def get_data_tranformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            clean_data_path=config.clean_data_path,
            augmented_data_path=config.augmented_data_path,
            new_data_path=config.new_data_path,
        )
        return data_transformation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.Models_03
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            target_columns=schema.target_column,
            training_columns=schema.training_columns,
            elastic_model_name=config.elastic_model_name,
            multinomial_model_name=config.multinomial_model_name,
            distilBERT_model_name=config.distilBERT_model_name,
            word2vector_model_name=config.word2vector_model_name,
            pipeline_ele_1=params.pipeline_ele_1,
            pipeline_ele_2=params.pipeline_ele_2,
            pipeline_ele_3=params.pipeline_ele_3,
        )
        return model_training_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.NBMultinomial
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name,
            all_params=params,
            mlflow_URI="https://dagshub.com/ukantjadia/Boolm-s-Level-Detection-A-MLOPS-Project.mlflow",
            target_column=schema.target_column,
            training_columns=schema.training_columns,
        )
        return model_evaluation_config
