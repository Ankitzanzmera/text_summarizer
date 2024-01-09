import sys
from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.utils.exception import CustomException
from text_summarizer.utils.logger import logger

class DataTransformationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e,sys)
        
STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)