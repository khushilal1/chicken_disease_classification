from src.cnnClassifier import logger

# logger.info("Welcone to my custom log")
from cnnClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e
