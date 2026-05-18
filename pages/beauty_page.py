from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class BeautyPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)


    # LOCATORS

    PRODUCTS = (By.CLASS_NAME, "product-base")

    SIZE = (By.XPATH, "(//div[contains(@class,'size-buttons-size-button')])[1]")

    # Locator for Add to Bag button on product details page
    ADD_TO_BAG = (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")



    def select_first_product(self):

        # Wait until all product cards are present on page
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTS)
        )


        products[0].click()

    def switch_to_product_tab(self):


        self.driver.switch_to.window(self.driver.window_handles[1])


    # Method to select size only if size exists
    def select_size_if_available(self):

        # try block because not all beauty products need size selection
        try:

            # Wait until size button becomes clickable
            size = self.wait.until(
                EC.element_to_be_clickable(self.SIZE)
            )

            size.click()

        except:
            pass


    # Method to click Add to Bag button
    def add_to_bag(self):


        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_BAG)
        )

        # Click Add to Bag
        add_btn.click()