import sys
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.utils.exception import CustomException
from text_summarizer.utils.logger import logger

class DataValidationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.is_valid()
        except Exception as e:
            raise CustomException(e,sys)
        
STAGE_NAME = "Data Validation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)