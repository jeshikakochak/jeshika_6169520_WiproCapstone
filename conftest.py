import logging
import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# suppress webdriver-manager logs
logging.getLogger("WDM").disabled = True
logging.getLogger("urllib3").disabled = True


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        driver = item.funcargs["driver"]

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        screenshot_path = f"screenshots/{item.name}.png"

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=item.name,
            attachment_type=allure.attachment_type.PNG
        )