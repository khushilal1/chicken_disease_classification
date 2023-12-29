import os
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
# file onn log
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running logs.log")
# making directory of logs

os.makedirs(log_dir, exist_ok=True)
# prisnting the info in terminal and given file path
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

 #exporting 
logger = logging.getLogger("cnnClassifierLogger")
