import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from utils.setup_logger import LogGen

logger = LogGen.loggen()




@allure.title("Search with Invalid Product Name")

def test_invalid_search_in_beauty(driver):

    wait = WebDriverWait(driver, 30)

    driver.get("https://www.myntra.com")
    driver.maximize_window()
    logger.info("Opened Myntra homepage")

    search_box = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "desktop-searchBar")
        )
    )

    invalid_product = "xyzlipbalm999"

    search_box.send_keys(invalid_product)
    search_box.send_keys(Keys.ENTER)
    logger.info("Entered invalid product in search")

    wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )

    search_heading = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title-title")
        )
    )

    assert invalid_product.lower() in search_heading.text.lower()
    logger.info("Invalid search testcase passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Invalid Search",
        attachment_type=allure.attachment_type.PNG
    )



@allure.title("Add Product Without Selecting Size")

def test_add_to_bag_without_selecting_size(driver):

    wait = WebDriverWait(driver, 30)

    driver.get(
        "https://www.myntra.com/serum-and-gel/minimalist/minimalist-vitamin-c-10-face-serum-for-glowing-skin-30-ml/14173102/buy"
    )
    driver.maximize_window()
    logger.info("Opened product page")

    sizes = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//p[contains(@class,'size-buttons-unified-size')]")
        )
    )

    assert len(sizes) > 1
    logger.info("Multiple size options verified")

    add_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )
    add_to_bag.click()
    logger.info("Clicked Add to Bag without selecting size")

    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'GO TO BAG')]")
            )
        )

        logger.error("Product added unexpectedly")
        assert False

    except TimeoutException:
        logger.info("Negative testcase passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Invalid Size Test",
        attachment_type=allure.attachment_type.PNG
    )