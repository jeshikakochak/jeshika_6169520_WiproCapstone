import logging
import os


def setup_logger():
    log_folder = "logs"

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logger = logging.getLogger("myntra_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/execution.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger