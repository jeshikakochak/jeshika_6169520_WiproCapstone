from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    BAG = (By.XPATH, "//span[contains(text(),'Bag')]")

    # methods

    # Method to open shopping cart
    def open_cart(self):
        bag = self.wait.until(
            EC.element_to_be_clickable(self.BAG)
        )
        bag.click()