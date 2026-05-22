from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BeautyPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    PRODUCTS = (By.CLASS_NAME, "product-base")
    SIZE = (By.XPATH, "(//div[contains(@class,'size-buttons-size-button')])[1]")
    ADD_TO_BAG = (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")

    def select_first_product(self):
        first_product = self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS)
        )
        first_product.click()

    def switch_to_product_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait.until(
            EC.presence_of_element_located(self.ADD_TO_BAG)
        )

    def select_size_if_available(self):
        try:
            size = self.wait.until(
                EC.element_to_be_clickable(self.SIZE)
            )
            size.click()

        except TimeoutException:
            print("No size required")

    def add_to_bag(self):
        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_BAG)
        )
        add_btn.click()