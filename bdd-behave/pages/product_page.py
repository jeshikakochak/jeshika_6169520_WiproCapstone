from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    SIZE = (
        By.XPATH,
        "(//div[contains(@class,'size-buttons-size-button')])[1]"
    )

    ADD_TO_BAG = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    GO_TO_BAG = (
        By.XPATH,
        "//span[contains(text(),'GO TO BAG')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Switch to newly opened product tab
    def switch_to_product_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    # Select size if available
    def select_size_if_available(self):
        try:
            size = self.wait.until(
                EC.element_to_be_clickable(
                    self.SIZE
                )
            )
            size.click()

        except:
            pass

    # Click Add to Bag button
    def add_to_bag(self):
        add_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_BAG
            )
        )
        add_btn.click()

    # Verify product added
    def is_product_added(self):
        go_to_bag = self.wait.until(
            EC.visibility_of_element_located(
                self.GO_TO_BAG
            )
        )
        return go_to_bag.is_displayed()