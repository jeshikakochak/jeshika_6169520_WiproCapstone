import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


def test_search_product_cart(driver):
    driver.get("https://www.myntra.com")

    wait = WebDriverWait(driver, 20)
    time.sleep(5)

    # search box
    search = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "desktop-searchBar")
        )
    )

    search.send_keys("lip balm")
    search.send_keys(Keys.ENTER)

    time.sleep(5)

    # first product
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )

    products[0].click()

    time.sleep(3)

    # switch tab
    driver.switch_to.window(driver.window_handles[1])

    # select size if available
    try:
        size = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class,'size-buttons-size-button')])[1]")
            )
        )
        size.click()
    except:
        pass

    # add to bag
    add_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )
    add_to_bag.click()

    time.sleep(3)

    # go to cart
    bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Bag')]")
        )
    )
    bag.click()

    time.sleep(3)

    assert "checkout/cart" in driver.current_url

