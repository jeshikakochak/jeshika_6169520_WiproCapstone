from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.beauty_locator import BeautyLocators


class BeautyPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_first_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.PRODUCTS
            )
        )

        product.click()

    def switch_tab(self):

        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    def select_size(self):

        try:
            size = self.wait.until(
                EC.element_to_be_clickable(
                    BeautyLocators.SIZE
                )
            )
            size.click()

        except TimeoutException:
            pass

    def add_to_bag(self):

        add = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.ADD_TO_BAG
            )
        )

        add.click()