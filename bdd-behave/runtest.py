import os
import shutil
from datetime import datetime

from utils.setup_logger import LogGen

logger = LogGen.loggen()


timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

logger.info("========================================")
logger.info("AUTOMATION EXECUTION STARTED")


# Delete old allure results
if os.path.exists("reports/allure-results"):
    logger.info(
        "Deleting old allure-results folder"
    )
    shutil.rmtree("reports/allure-results")


# Delete old report
if os.path.exists("reports/allure-report"):
    logger.info(
        "Deleting old allure-report folder"
    )
    shutil.rmtree("reports/allure-report")


# Run Behave
logger.info("Starting Behave Execution")

behave_status = os.system("behave")

logger.info(
    f"Behave completed with status code: {behave_status}"
)


# Generate report
logger.info("Generating Allure Report")

allure_generate_status = os.system(
    "allure generate reports/allure-results "
    "-o reports/allure-report --clean"
)

logger.info(
    f"Allure report generated with status code: "
    f"{allure_generate_status}"
)


# Open report automatically
logger.info("Opening Allure Report")

os.system(
    "allure open reports/allure-report"
)

logger.info("AUTOMATION EXECUTION COMPLETED")
logger.info("========================================")