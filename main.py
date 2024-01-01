from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_2_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from cnnClassifier.pipeline.stage_3_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e


# for training data

STAGE_NAME = "Prepare Base model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e


# for traininig

STAGE_NAME = "Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e
