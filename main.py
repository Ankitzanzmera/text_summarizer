import sys
from text_summarizer.utils.logger import logger
from text_summarizer.utils.exception import CustomException

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)
        logger.info("in the main.py file")
