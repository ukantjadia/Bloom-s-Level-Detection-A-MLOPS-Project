from blooms import logger
from blooms.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from blooms.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from blooms.pipeline.stage_03_data_transformation import DataTrnsformationPipeline
from blooms.pipeline.stage_04_model_training import ModelTrainingPipeline
from blooms.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


logger.info("Welcome to the logs of blooms level detection a MLops project ")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    ingestion = DataIngestionTrainingPipeline()
    ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    validation = DataValidationTrainingPipeline()
    validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    transformation = DataTrnsformationPipeline()
    transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    training = ModelTrainingPipeline()
    training.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    evaluation = ModelEvaluationPipeline()
    evaluation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e