from src.winequalitypred import logger 
from src.winequalitypred.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.winequalitypred.pipeline.data_validation_pipeline import DataValidationPipeline  
from src.winequalitypred.pipeline.data_transformation_pipeline import DataTransformationPipeline 
from src.winequalitypred.pipeline.model_trainer_pipeline import ModelTrainerPipeline 

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.initiate_data_ingestion()
   logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationPipeline()
   data_ingestion.initiate_data_validation()
   logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationPipeline()
   data_ingestion.initiate_data_transformation()
   logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 