from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_lipbalm_products(driver):

    wait = WebDriverWait(driver, 20)

    # Open Myntra
    driver.get("https://www.myntra.com")

    # Locate Beauty menu
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    # Hover on Beauty
    actions = ActionChains(driver)
    actions.move_to_element(beauty_menu).pause(2).perform()

    # Click Lip Balm
    lip_balm = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    lip_balm.click()

    # Validation
    assert "lip-balm" in driver.current_url.lower()