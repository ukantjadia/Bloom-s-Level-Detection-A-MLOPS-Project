from blooms.config.configuration import ConfigurationManager
from blooms.components.model_training import ModelTrainer
from blooms import logger

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\n x=======x")
    except Exception as e:
        logger.exception(e)
        raise e
