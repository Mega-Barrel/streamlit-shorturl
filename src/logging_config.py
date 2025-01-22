"""Logger Module"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Define the log directory and file name
LOG_DIR = "logs"
LOG_FILE = "app.log"

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    """
    Sets up logging configuration to save logs to a text file.
    Uses a RotatingFileHandler to limit log file size.
    """
    log_file_path = os.path.join(LOG_DIR, LOG_FILE)

    # Create a logger
    logger = logging.getLogger("StreamlitApp")
    logger.setLevel(logging.INFO)

    # Create a file handler with rotation (max size 5MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=5 * 1024 * 1024, backupCount=3
    )
    file_handler.setLevel(logging.INFO)

    # Create a console handler (optional, for viewing logs in the terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define a log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
