from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_beauty_navigation(driver):

    wait = WebDriverWait(driver, 20)

    # Open Myntra
    driver.get("https://www.myntra.com")

    # Find Beauty menu
    beauty_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-group='beauty']")
        )
    )

    # Hover properly
    actions = ActionChains(driver)
    actions.move_to_element(beauty_menu).pause(3).perform()

    # Check a real dropdown option
    lip_balm = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='Lip Balm']")
        )
    )

    assert lip_balm.is_displayed()
