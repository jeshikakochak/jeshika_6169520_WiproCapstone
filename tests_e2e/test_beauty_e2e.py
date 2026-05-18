from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


def test_beauty_end_to_end(driver):

    wait = WebDriverWait(driver, 60)

    driver.get("https://www.myntra.com")
    driver.maximize_window()

    # Hover Beauty
    beauty_menu = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )
    ActionChains(driver).move_to_element(beauty_menu).pause(2).perform()

    # Click Lip Balm
    lip_balm = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )
    lip_balm.click()

    # Select product
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )
    products[2].click()

    # Switch to product tab
    driver.switch_to.window(driver.window_handles[-1])

    # Size if needed
    try:
        size = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class,'size-buttons')])[1]")
            )
        )
        size.click()
    except:
        pass

    # Add to Bag
    add_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )
    add_to_bag.click()

    # Go to Bag
    go_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'GO TO BAG')]")
        )
    )
    go_to_bag.click()

    # Quantity
    qty_dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'itemComponents-base-quantity')]")
        )
    )
    qty_dropdown.click()

    qty_two = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//div[contains(@class,'dialogs-base-item')])[2]")
        )
    )
    qty_two.click()

    # Donation ₹10
    donate = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'pillView-base-textStyle') and contains(.,'₹10')]")
        )
    )
    ActionChains(driver).move_to_element(donate).pause(1).click().perform()

    # Wait for PLACE ORDER to be re-enabled
    place_order = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'PLACE ORDER')]")
        )
    )

    # Retry click
    for _ in range(3):
        try:
            ActionChains(driver).move_to_element(place_order).pause(1).click().perform()
            break
        except ElementClickInterceptedException:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(.,'PLACE ORDER')]")
                )
            )

    # Wait for login page navigation
    wait.until(
        lambda d:
            "login" in d.current_url.lower()
            or "checkout" in d.current_url.lower()
            or "auth" in d.current_url.lower()
    )

    assert True