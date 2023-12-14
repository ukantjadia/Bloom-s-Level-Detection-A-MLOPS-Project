from blooms import logger 
from blooms.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logger.info("Welcome to the logs of blooms level detection a MLops project ")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e