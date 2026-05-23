from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from locators.beauty_locator import BeautyLocators


class BeautyPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Open first product from listing
    def open_first_product(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                BeautyLocators.PRODUCTS
            )
        )

        products = self.driver.find_elements(
            *BeautyLocators.PRODUCTS
        )

        self.driver.execute_script(
            "arguments[0].click();",
            products[0]
        )

    # Open third product from listing
    def open_third_product(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                BeautyLocators.PRODUCTS
            )
        )

        products = self.driver.find_elements(
            *BeautyLocators.PRODUCTS
        )

        self.driver.execute_script(
            "arguments[0].click();",
            products[2]
        )

        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

    # Switch to product tab
    def switch_tab(self):

        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(d.window_handles) > 1
            )

            self.driver.switch_to.window(
                self.driver.window_handles[-1]
            )

        except:
            pass

    # Select size if available
    def select_size(self):

        try:
            size = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    BeautyLocators.SIZE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                size
            )

        except:
            pass

    # Add to bag
    def add_to_bag(self):

        add = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.ADD_TO_BAG
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

    # Go to bag
    def go_to_bag(self):

        bag = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.GO_TO_BAG
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bag
        )

    # Verify cart
    def verify_cart(self):

        self.wait.until(
            EC.visibility_of_element_located(
                BeautyLocators.CART_ITEM
            )
        )

    # Change quantity
    def change_quantity(self):

        qty = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.QUANTITY_DROPDOWN
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            qty
        )

        qty2 = self.wait.until(
            EC.visibility_of_element_located(
                BeautyLocators.QUANTITY_TWO
            )
        )

        try:
            qty2.click()

        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].click();",
                qty2
            )

    # Select donation
    def select_donation(self):

        donate = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.DONATION
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            donate
        )

    # Place order
    def place_order(self):

        place = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.PLACE_ORDER
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            place
        )

    # Verify login redirect
    def verify_login_redirect(self):

        self.wait.until(
            lambda d: "login" in d.current_url.lower()
        )