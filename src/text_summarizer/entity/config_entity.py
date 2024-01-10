from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_validation_status_file: str
    data_validation_required_file: list
    data_path:Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    tokenizer_name:str
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    transformed_data_path: Path
    model_ckpt: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    transformed_data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path