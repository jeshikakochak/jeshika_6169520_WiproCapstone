import logging
import os
from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("reports/logs"):
            os.makedirs("reports/logs")

        log_file = datetime.now().strftime(
            "reports/logs/automation_%Y-%m-%d_%H-%M-%S.log"
        )

        logger = logging.getLogger("bdd_logger")
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers():

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