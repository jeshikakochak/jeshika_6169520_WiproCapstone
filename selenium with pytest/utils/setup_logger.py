import logging
import os
from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        # prevent duplicate handlers only for this logger
        if not logger.handlers:

            log_file = datetime.now().strftime(
                "logs/automation_%Y-%m-%d_%H-%M-%S.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(message)s"
            )

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger