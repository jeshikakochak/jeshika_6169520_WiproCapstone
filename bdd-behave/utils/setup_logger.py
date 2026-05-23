import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("bdd_logger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:

            file_handler = logging.FileHandler(
                "logs/test.log",
                mode="a",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger