import logging
import os

def setup_logger(log_file='test_execution.log'):
    """Set up logging to a specified log file and console."""

    log_file_path = os.path.join("logs", log_file)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w') as _:
            pass

    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # Configure the root logger
    logging.basicConfig(level=logging.INFO, format=log_format, filename=log_file_path)

    # Adding a console handler to also print log messages to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(console_handler)

def log(message, level="INFO", app_name=None):
    if app_name:
        message = f"[{app_name}] {message}"

    if level in logging._nameToLevel:
        logging.log(logging._nameToLevel[level], message)
    else:
        raise ValueError("Invalid log level")
