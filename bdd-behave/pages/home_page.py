from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.beauty_locator import BeautyLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_homepage(self, url):
        self.driver.get(url)

    def search_product(self, product):

        search = self.wait.until(
            EC.visibility_of_element_located(
                BeautyLocators.SEARCH_BOX
            )
        )

        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)

    def hover_beauty_menu(self):

        beauty = self.wait.until(
            EC.visibility_of_element_located(
                BeautyLocators.BEAUTY_MENU
            )
        )

        ActionChains(self.driver).move_to_element(beauty).pause(2).perform()