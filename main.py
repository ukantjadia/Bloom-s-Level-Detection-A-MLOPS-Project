from blooms import logger
from blooms.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from blooms.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


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
