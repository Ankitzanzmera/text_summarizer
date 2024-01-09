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