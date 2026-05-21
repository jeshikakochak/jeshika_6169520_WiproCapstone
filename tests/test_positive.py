import allure
import pytest
from utils.setup_logger import LogGen

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = LogGen.loggen()




@allure.title("Navigate to Beauty Menu")

def test_beauty_navigation(driver):

    wait = WebDriverWait(driver, 20)

    logger.info("Opening Myntra homepage")
    driver.get("https://www.myntra.com")

    logger.info("Locating Beauty menu")
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    logger.info("Hovering over Beauty menu")
    ActionChains(driver).move_to_element(beauty_menu).pause(3).perform()

    logger.info("Checking Lip Balm visibility")
    lip_balm = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    assert lip_balm.is_displayed()
    logger.info("Beauty navigation test passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Beauty Navigation",
        attachment_type=allure.attachment_type.PNG
    )



@allure.title("Open Product from Homepage")

def test_homepage_to_beauty_product(driver):

    wait = WebDriverWait(driver, 40)

    logger.info("Opening Myntra homepage")
    driver.get("https://www.myntra.com")
    driver.maximize_window()

    try:
        logger.info("Checking popup")
        popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'desktop-iconClose')]")
            )
        )
        popup.click()
        logger.info("Popup closed")

    except:
        logger.info("No popup found")

    logger.info("Hovering over Beauty menu")
    beauty_menu = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    ActionChains(driver).move_to_element(beauty_menu).pause(2).perform()

    logger.info("Clicking Lip Balm")
    lip_balm = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    driver.execute_script("arguments[0].click();", lip_balm)

    logger.info("Opening first product")
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )

    products[0].click()

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    logger.info("Waiting for product page")
    product_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "pdp-title")
        )
    )

    assert product_title.is_displayed()
    logger.info("Homepage to product test passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Homepage Product",
        attachment_type=allure.attachment_type.PNG
    )



@allure.title("Open Lip Balm Listings")

def test_open_lipbalm_products(driver):

    wait = WebDriverWait(driver, 40)

    logger.info("Opening Myntra homepage")
    driver.get("https://www.myntra.com")
    driver.maximize_window()

    try:
        logger.info("Checking popup")
        popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'desktop-iconClose')]")
            )
        )
        popup.click()

    except:
        logger.info("No popup found")

    logger.info("Hovering over Beauty menu")
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    ActionChains(driver).move_to_element(beauty_menu).perform()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    logger.info("Opening Lip Balm listing page")
    lip_balm = driver.find_element(By.XPATH, "//a[text()='Lip Balm']")
    driver.execute_script("arguments[0].click();", lip_balm)

    wait.until(
        EC.url_contains("lip-balm")
    )

    assert "lip-balm" in driver.current_url.lower()
    logger.info("Lip Balm listing test passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Lip Balm Listings",
        attachment_type=allure.attachment_type.PNG
    )


@allure.title("Add Lip Balm to Cart")

def test_add_lipbalm_to_cart(driver):

    wait = WebDriverWait(driver, 30)

    logger.info("Opening Myntra homepage")
    driver.get("https://www.myntra.com")
    driver.maximize_window()

    logger.info("Hovering over Beauty menu")
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    ActionChains(driver).move_to_element(beauty_menu).pause(3).perform()

    logger.info("Opening Lip Balm category")
    lip_balm = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    driver.execute_script("arguments[0].click();", lip_balm)

    logger.info("Selecting product")
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )

    products[2].click()
    driver.switch_to.window(driver.window_handles[-1])

    wait.until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    try:
        logger.info("Selecting size if required")
        option = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[contains(@class,'size-buttons-size-button') or contains(@class,'size-buttons-unified-size')])[1]"
                )
            )
        )
        option.click()

    except:
        logger.info("No size selection required")

    logger.info("Adding product to cart")
    add_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )
    add_to_bag.click()

    logger.info("Verifying cart")
    go_to_bag = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'GO TO BAG')]")
        )
    )

    assert go_to_bag.is_displayed()
    logger.info("Add to cart test passed")

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Lip Balm Cart",
        attachment_type=allure.attachment_type.PNG
    )