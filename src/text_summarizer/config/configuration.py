from text_summarizer.constants import *
from text_summarizer.utils.common import create_directories,read_yaml
from text_summarizer.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig)

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH) -> None:
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        temp_config = self.config.data_ingestion
        create_directories([temp_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=temp_config.root_dir,
            source= temp_config.source,
            local_data_file = temp_config.local_data_file,
            unzip_dir = temp_config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        temp_config = self.config.data_validation
        create_directories([temp_config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= Path(temp_config.root_dir),
            data_validation_status_file = temp_config.data_validation_status_file,
            data_validation_required_file = temp_config.data_validation_required_file,
            data_path = temp_config.unzip_dir
        )

        return data_validation_config