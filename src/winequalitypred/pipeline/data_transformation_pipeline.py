from src.winequalitypred.config.configuration import ConfigurationManager
from src.winequalitypred.components.data_transformation import DataTransformation
from src.winequalitypred import logger

from pathlib import Path


STAGE_NAME="Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
            
        except Exception as e:
            print(e) 