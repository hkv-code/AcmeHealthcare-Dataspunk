import logging
import logging.handlers
import os
from datetime import datetime

def configure_logger():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a directory for logs if it doesn't exist
    if not os.path.exists('../logs'):
        os.makedirs('../logs')

    # Create a file handler that logs even debug messages
    # Include current datetime in the log filename
    log_filename = f'../logs/log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    file_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Also add the handler to the root logger
    logging.getLogger().addHandler(file_handler)
