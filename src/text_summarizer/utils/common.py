import sys,os
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any
from text_summarizer.utils.exception import CustomException
from text_summarizer.utils.logger import logger

@ensure_annotations
def read_yaml(filepath:Path) -> ConfigBox:
    try:    
        with open(filepath,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is Empty")
    except Exception as e:
        raise CustomException(e,sys)

def create_directories(path_to_directory: list) -> None:
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        logger.info(f"{path} Directory Created Successfully")