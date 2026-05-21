from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    SEARCH_BOX = (By.CLASS_NAME, "desktop-searchBar")
    BEAUTY_MENU = (By.XPATH, "//a[contains(text(),'Beauty')]")

    def open_homepage(self):
        self.driver.get("https://www.myntra.com/")

    def search_product(self, product_name):
        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search.clear()
        search.send_keys(product_name)
        search.send_keys(Keys.ENTER)

    def open_beauty_menu(self):
        beauty = self.wait.until(
            EC.visibility_of_element_located(self.BEAUTY_MENU)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(beauty).pause(2).perform()