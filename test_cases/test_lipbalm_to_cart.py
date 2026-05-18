from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_lipbalm_to_cart(driver):

    wait = WebDriverWait(driver, 25)

    # Open Myntra
    driver.get("https://www.myntra.com")

    # Hover over Beauty menu
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    actions = ActionChains(driver)
    actions.move_to_element(beauty_menu).pause(2).perform()

    # Click Lip Balm
    lip_balm = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )
    lip_balm.click()

    # Wait for products
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-base")
        )
    )

    # Click a product (avoid first if unstable)
    products[2].click()

    # Switch to product tab
    driver.switch_to.window(driver.window_handles[-1])

    # Wait for product page to load
    wait.until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    # Select size / variant / option if required
    try:
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
        pass

    # Click Add to Bag
    add_to_bag = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'ADD TO BAG')]")
        )
    )
    add_to_bag.click()

    # Validate product added
    go_to_bag = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'GO TO BAG')]")
        )
    )

    assert go_to_bag.is_displayed()