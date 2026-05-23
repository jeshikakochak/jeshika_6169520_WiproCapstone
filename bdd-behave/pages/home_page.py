from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.beauty_locator import BeautyLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Open Myntra homepage
    def open_homepage(self, url):
        self.driver.get(url)

    # Close popup if popup appears
    def close_popup_if_present(self):

        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[contains(@class,'desktop-iconClose')]"
                    )
                )
            )

            popup.click()

        except:
            pass

    # Search product in search box
    def search_product(self, product):

        search = self.wait.until(
            EC.visibility_of_element_located(
                BeautyLocators.SEARCH_BOX
            )
        )

        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)

    # Hover over Beauty menu
    def hover_beauty_menu(self):

        beauty = self.wait.until(
            EC.element_to_be_clickable(
                BeautyLocators.BEAUTY_MENU
            )
        )

        ActionChains(self.driver).move_to_element(
            beauty
        ).pause(2).perform()

    # Select category dynamically
    def select_category(self, category):

        category_element = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//a[text()='{category}']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            category_element
        )