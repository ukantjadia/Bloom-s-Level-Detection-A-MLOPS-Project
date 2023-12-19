from blooms.config.configuration import ConfigurationManager
from blooms.components.data_transformation import DataTrnsformation
from blooms import logger

STAGE_NAME = "Data Transformation Stage"


class DataTrnsformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transfermation_config = config.get_data_tranformation_config()
        data_transfermation = DataTrnsformation(config=data_transfermation_config)
        data_transfermation.data_preprocessing()
        # data_transfermation.data_augmentation()
        data_transfermation.tokenization()
        data_transfermation.train_test_splitting()


if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTrnsformationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\n x=======x")
    except Exception as e:
        logger.exception(e)
        raise e
