import logging
from datetime import datetime
import os,sys

log_file_dir_name = f"{datetime.now().strftime('%d_%m_%y')}"
dir_path = os.path.join(os.getcwd(),"logs",log_file_dir_name)
os.makedirs(dir_path,exist_ok=True)

log_file_name = f"{datetime.now().strftime('%H_%M_%S')}"
LOG_FILE_PATH = os.path.join(dir_path,log_file_name)

logging.basicConfig(
    level=logging.INFO,
    format = " [ %(asctime)s ] - %(lineno)d - %(module)s - %(message)s",
    handlers = [
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout),
    ]
)

logger = logging.getLogger("text_summarizer")