from text_summarizer.constants import *
from text_summarizer.utils.common import create_directories,read_yaml
from text_summarizer.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH,params_filepath = PARAMS_FILEPATH) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
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
            data_path = temp_config.data_path
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        temp_config = self.config.data_transformation
        create_directories([temp_config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = temp_config.root_dir,
            tokenizer_name = temp_config.tokenizer_name,
            data_path = temp_config.data_path 
        )
        return data_transformation_config
    
    def get_model_trainer_config(self):
        temp_config = self.config.model_trainer
        params = self.params.TrainingArguments
        create_directories([temp_config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = temp_config.root_dir,
            transformed_data_path = temp_config.transformed_data_path,
            model_ckpt = temp_config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config