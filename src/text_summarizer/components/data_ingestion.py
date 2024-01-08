import sys,os
import gdown
from zipfile import ZipFile
from text_summarizer.utils.logger import logger
from text_summarizer.utils.exception import CustomException
from text_summarizer.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                gdown.download(self.config.source, self.config.local_data_file)
                logger.info("Zip file downloaded successfully")
            else:
                logger.info("Zip file is already Existed")
        except Exception as e:
            raise CustomException(e,sys)

    def extract_file(self):
        try:
            if os.path.exists(self.config.unzip_dir):
                logger.info("File is Already Extracted")
            else:
                with ZipFile(self.config.local_data_file,'r') as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                logger.info('Zip file extracted Successfully')
        except Exception as e:
            raise CustomException(e,sys)
    