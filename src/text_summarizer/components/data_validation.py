import sys,os
from text_summarizer.entity.config_entity import DataValidationConfig
from text_summarizer.utils.logger import logger
from text_summarizer.utils.exception import CustomException

class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config = config
    
    def is_valid(self):
        validation_status = None
        all_required_files = self.config.data_validation_required_file
        file_that_exists = os.listdir(self.config.data_path)
        try:
            for file in all_required_files:
                if file not in file_that_exists:
                    validation_status = False
                    with open(self.config.data_validation_status_file,'w') as file_obj:
                        file_obj.write(f'Validation Status = {validation_status}')
                        logger.info(f"Validation Status is {validation_status}")
                        raise SystemExit
                else:
                    validation_status = True
                    with open(self.config.data_validation_status_file,'w') as file_obj:
                        file_obj.write(f'Validation Status = {validation_status}')
            logger.info(f"Validation Status is {validation_status}")
        except Exception as e:
            raise CustomException(e,sys)