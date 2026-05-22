from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    BAG = (
        By.XPATH,
        "//span[contains(text(),'Bag')]"
    )

    CART_HEADING = (
        By.XPATH,
        "//div[contains(text(),'Shopping Bag')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Open shopping cart
    def open_cart(self):
        bag = self.wait.until(
            EC.element_to_be_clickable(
                self.BAG
            )
        )
        bag.click()

    # Verify cart page opened
    def is_cart_opened(self):
        cart = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_HEADING
            )
        )
        return cart.is_displayed()