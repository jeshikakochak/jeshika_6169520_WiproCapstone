import os
import allure

from datetime import datetime
from utils.setup_logger import LogGen

logger = LogGen.loggen()


class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(
            driver,
            screenshot_name="screenshot"
    ):
        # SCREENSHOT DIRECTORY

        screenshot_dir = \
            "reports/screenshots"

        if not os.path.exists(
                screenshot_dir
        ):
            os.makedirs(
                screenshot_dir
            )

        # TIMESTAMP

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # CLEAN FILE NAME

        clean_name = \
            screenshot_name.replace(
                " ",
                "_"
            )

        # FINAL PATH

        screenshot_path = (
            f"{screenshot_dir}/"
            f"{clean_name}_{timestamp}.png"
        )

        # SAVE SCREENSHOT

        driver.save_screenshot(
            screenshot_path
        )

        logger.info(
            f"Screenshot saved at : "
            f"{screenshot_path}"
        )

        allure.attach.file(
            screenshot_path,
            name=clean_name,
            attachment_type=allure.attachment_type.PNG
        )

        return screenshot_path