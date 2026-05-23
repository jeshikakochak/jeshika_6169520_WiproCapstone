# import allure
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from utils.config_reader import ConfigReader
from utils.setup_logger import LogGen

logger = LogGen.loggen()



@given("user opens Myntra homepage for test cases")
def step_home(context):

    logger.info("Opening Myntra homepage")

    context.home = HomePage(context.driver)
    context.home.open_homepage(
        ConfigReader.get_base_url()
    )



@when("user closes popup for test cases")
def step_popup(context):

    logger.info("Closing popup if present")

    context.home.close_popup_if_present()



@when("user hovers over beauty menu for test cases")
def step_hover(context):

    logger.info("Hovering over Beauty menu")

    context.home.hover_beauty_menu()



@then("Lip Balm category should be visible")
def step_visible(context):

    logger.info("Checking Lip Balm category visibility")

    context.home.select_category("Lip Balm")



@when("user opens Lip Balm category for test cases")
def step_category(context):

    logger.info("Opening Lip Balm category")

    context.home.select_category("Lip Balm")

    WebDriverWait(context.driver, 10).until(
        EC.url_contains("lip-balm")
    )



@when("user opens first product for test cases")
def step_product(context):

    logger.info("Opening first product")

    context.beauty = BeautyPage(context.driver)
    context.beauty.open_first_product()



@then("product page should open")
def step_page(context):

    logger.info("Verifying product page")

    assert "myntra.com" in context.driver.current_url.lower()



@then("Lip Balm listing page should open")
def step_listing(context):

    logger.info("Verifying Lip Balm listing page")

    assert "lip-balm" in context.driver.current_url.lower()



@when("user opens third product for test cases")
def step_third_product(context):

    logger.info("Opening third product")

    context.beauty = BeautyPage(context.driver)
    context.beauty.open_third_product()



@when("user selects size if available for test cases")
def step_size(context):

    logger.info("Selecting size if available")

    context.beauty.select_size()


@when("user adds product to bag for test cases")
def step_add(context):

    logger.info("Adding product to bag")

    context.beauty.add_to_bag()



@then("product should be added to cart")
def step_cart(context):

    assert (
        "GO TO BAG" in context.driver.page_source
        or "Bag" in context.driver.page_source
        or "Added to Bag" in context.driver.page_source
    )

@when("user searches invalid product")
def step_invalid(context):

    invalid_product = "xyzlipbalm999"

    logger.info("Searching invalid product")

    context.home.search_product(
        invalid_product
    )

    context.invalid_product = invalid_product


@then("invalid search results should be displayed")
def step_invalid_result(context):

    logger.info("Verifying invalid search results")

    assert (
        context.invalid_product.lower()
        in context.driver.page_source.lower()
    )



@given("user opens product page")
def step_product_page(context):

    logger.info("Opening product page")

    context.driver.get(
        "https://www.myntra.com/serum-and-gel/minimalist/minimalist-vitamin-c-10-face-serum-for-glowing-skin-30-ml/14173102/buy"
    )

@when("user clicks add to bag without selecting size")
def step_negative(context):

    logger.info("Clicking Add to Bag without selecting size")

    context.beauty = BeautyPage(context.driver)
    context.beauty.add_to_bag()



@then("product should not be added")
def step_not_added(context):

    logger.info("Verifying negative scenario")

    assert "GO TO BAG" not in context.driver.page_source

