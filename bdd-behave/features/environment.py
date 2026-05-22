from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.setup_logger import LogGen
import configparser


logger = LogGen.loggen()


def before_scenario(context, scenario):

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    browser = config["DEFAULT"]["browser"]

    if browser.lower() == "chrome":

        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    context.driver.maximize_window()
    logger.info("Browser launched")


def after_scenario(context, scenario):

    context.driver.quit()
    logger.info("Browser closed")