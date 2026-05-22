import os
import pytest
import allure
import chromedriver_autoinstaller
from selenium import webdriver


@pytest.fixture()
def driver():

    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(30)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and "driver" in item.funcargs:

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