import pytest
import allure
from utils.csv_reader import get_csv_data
from utils.setup_logger import LogGen

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

logger = LogGen.loggen()


@pytest.mark.parametrize(
    "product",
    get_csv_data("data/product.csv")
)
@allure.title("Beauty End-to-End Test")
@allure.description("Complete end-to-end beauty product purchase flow from homepage to login redirect.")
def test_beauty_end_to_end(driver, product):

    wait = WebDriverWait(driver, 60)

    logger.info(f"Starting E2E test for {product}")

    driver.get("https://www.myntra.com")
    driver.maximize_window()

    assert "myntra" in driver.current_url.lower(), \
        f"Homepage not opened. Current URL: {driver.current_url}"

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Homepage",
        attachment_type=allure.attachment_type.PNG
    )

    # Close popup if present
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

    # Hover beauty menu
    logger.info("Hovering over Beauty menu")
    beauty = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    assert beauty.is_displayed(), \
        "Beauty menu is not visible"

    ActionChains(driver).move_to_element(beauty).perform()

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Beauty Hover",
        attachment_type=allure.attachment_type.PNG
    )

    # Dynamic product from CSV
    logger.info(f"Selecting product category: {product}")

    product_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//a[text()='{product}']")
        )
    )

    assert product_menu.is_displayed(), \
        f"{product} category not visible"

    driver.execute_script("arguments[0].click();", product_menu)

    # Wait for listing
    logger.info("Waiting for product listings")
    wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//li[contains(@class,'product-base')]//a")
        )
    )

    product_links = driver.find_elements(
        By.XPATH,
        "//li[contains(@class,'product-base')]//a"
    )

    assert len(product_links) > 0, \
        "No products found on listing page"

    logger.info("Opening first product")
    driver.execute_script("arguments[0].click();", product_links[0])

    # Handle new tab
    try:
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        driver.switch_to.window(driver.window_handles[-1])
        logger.info("Switched to new tab")

    except:
        logger.info("Same tab navigation")

    # Product page load
    logger.info("Waiting for product page")
    wait.until(
        EC.any_of(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "pdp-title")
            ),
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
            )
        )
    )

    add_button_check = driver.find_elements(
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    assert len(add_button_check) > 0, \
        "Product page did not load properly"

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Product Page",
        attachment_type=allure.attachment_type.PNG
    )

    # Size selection if needed
    try:
        logger.info("Selecting size")
        size = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[contains(@class,'size-buttons-size-button') or contains(@class,'size-buttons-unified-size')])[1]"
                )
            )
        )

        assert size.is_displayed(), \
            "Size option found but not visible"

        driver.execute_script("arguments[0].click();", size)

    except:
        logger.info("No size selection needed")

    # Add to bag
    logger.info("Adding product to bag")
    add = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )

    assert add.is_displayed(), \
        "ADD TO BAG button not visible"

    driver.execute_script("arguments[0].click();", add)

    # Go to bag
    logger.info("Going to bag")
    bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'GO TO BAG')]")
        )
    )

    assert bag.is_displayed(), \
        "GO TO BAG button not visible. Product may not have been added."

    driver.execute_script("arguments[0].click();", bag)

    # Wait for cart
    logger.info("Waiting for cart")
    cart_item = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "itemContainer-base-item")
        )
    )

    assert cart_item.is_displayed(), \
        "Cart page did not load or item not added"

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Cart Page",
        attachment_type=allure.attachment_type.PNG
    )

    # Quantity dropdown
    logger.info("Opening quantity dropdown")
    qty = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'itemComponents-base-quantity')]")
        )
    )

    assert qty.is_displayed(), \
        "Quantity dropdown not visible"

    driver.execute_script("arguments[0].click();", qty)

    # Quantity = 2
    logger.info("Changing quantity to 2")
    qty2 = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//div[contains(@class,'dialogs-base-item')])[2]")
        )
    )

    assert qty2.is_displayed(), \
        "Quantity option 2 not visible"

    try:
        qty2.click()

    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", qty2)

    # Donation
    logger.info("Selecting donation")
    donate = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(.,'₹10')]")
        )
    )

    assert donate.is_displayed(), \
        "Donation option not visible"

    driver.execute_script("arguments[0].click();", donate)

    # Place order
    logger.info("Clicking Place Order")
    place = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'PLACE ORDER')]")
        )
    )

    assert place.is_displayed(), \
        "PLACE ORDER button not visible"

    driver.execute_script("arguments[0].click();", place)

    # Login redirect
    logger.info("Waiting for login redirect")
    wait.until(
        lambda d: "login" in d.current_url.lower()
    )

    assert "login" in driver.current_url.lower(), \
        f"Login redirect failed. Current URL: {driver.current_url}"

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Login Redirect",
        attachment_type=allure.attachment_type.PNG
    )

    logger.info("E2E test passed successfully")