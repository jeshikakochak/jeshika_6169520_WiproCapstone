import allure
import os
from selenium import webdriver
from utils.config_reader import ConfigReader
from utils.setup_logger import LogGen

logger = LogGen.loggen()


def before_scenario(context, scenario):

    logger.info("===================================")
    logger.info(f"STARTING SCENARIO: {scenario.name}")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    if ConfigReader.get_headless():
        options.add_argument("--headless=new")

    context.driver = webdriver.Chrome(
        options=options
    )

    context.driver.implicitly_wait(
        ConfigReader.get_implicit_wait()
    )

    context.driver.set_page_load_timeout(
        ConfigReader.get_timeout()
    )


def after_scenario(context, scenario):

    logger.info(f"SCENARIO STATUS: {scenario.status}")

    # Screenshot
    if hasattr(context, "driver"):

        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"{scenario.name}_Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    # FULL LOGGER ATTACHMENT
    try:

        for handler in logger.handlers:
            handler.flush()

        log_file = "logs/test.log"

        if os.path.exists(log_file):

            allure.attach.file(
                log_file,
                name="Full Execution Logger",
                attachment_type=allure.attachment_type.TEXT
            )

            logger.info("Log file attached to Allure")

    except Exception as e:

        logger.error(f"Log attachment failed: {e}")

    if hasattr(context, "driver"):
        context.driver.quit()

    logger.info(f"COMPLETED SCENARIO: {scenario.name}")
    logger.info("===================================")