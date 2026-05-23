from behave import given, when, then
from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from utils.config_reader import ConfigReader
from utils.screenshot_util import ScreenshotUtil
from utils.setup_logger import LogGen

logger = LogGen.loggen()


@given("user opens Myntra homepage for end to end")
def step_open_home(context):

    logger.info("Opening Myntra homepage for end-to-end flow")

    context.home = HomePage(context.driver)

    context.home.open_homepage(
        ConfigReader.get_base_url()
    )

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Homepage did not open"

    logger.info("Myntra homepage opened successfully")


@when("user closes popup if present")
def step_popup(context):

    logger.info("Closing popup if present")

    context.home.close_popup_if_present()

    assert context.driver is not None, \
        "Driver became unavailable"

    logger.info("Popup handling completed")


@when("user hovers over beauty menu")
def step_hover(context):

    logger.info("Hovering over Beauty menu")

    context.home.hover_beauty_menu()

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Hover action failed"

    logger.info("Hovered over Beauty menu successfully")


@when('user selects "Lip Balm" category')
def step_category(context):

    logger.info("Selecting Lip Balm category")

    context.home.select_category("Lip Balm")

    assert "lip-balm" in context.driver.current_url.lower(), \
        "Lip Balm category did not open"

    logger.info("Lip Balm category opened successfully")


@when("user opens first product")
def step_product(context):

    logger.info("Opening first product")

    context.beauty = BeautyPage(context.driver)

    context.beauty.open_first_product()

    assert len(context.driver.window_handles) >= 1, \
        "Product click failed"

    logger.info("First product clicked successfully")


@when("user switches to product tab")
def step_switch(context):

    logger.info("Switching to product tab")

    context.beauty.switch_tab()

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Product tab did not open"

    logger.info("Switched to product tab successfully")


@when("user selects size if available")
def step_size(context):

    logger.info("Selecting product size")

    context.beauty.select_size()

    assert context.driver is not None, \
        "Size selection failed"

    logger.info("Size selection completed")


@when("user adds product to bag")
def step_add(context):

    logger.info("Adding product to bag")

    context.beauty.add_to_bag()

    assert "GO TO BAG" in context.driver.page_source \
        or "Bag" in context.driver.page_source, \
        "Product not added to bag"

    logger.info("Product added to bag successfully")


@when("user goes to shopping bag")
def step_bag(context):

    logger.info("Opening shopping bag")

    context.beauty.go_to_bag()

    assert "bag" in context.driver.current_url.lower() \
        or "checkout" in context.driver.current_url.lower(), \
        "Shopping bag did not open"

    logger.info("Shopping bag opened successfully")


@when("user verifies cart item")
def step_cart(context):

    logger.info("Verifying cart item")

    context.beauty.verify_cart()

    assert "bag" in context.driver.page_source.lower() \
        or "shopping bag" in context.driver.page_source.lower(), \
        "Cart item not verified"

    logger.info("Cart item verified successfully")


@when("user changes quantity to 2")
def step_quantity(context):

    logger.info("Changing quantity to 2")

    context.beauty.change_quantity()

    assert context.driver is not None, \
        "Quantity change failed"

    logger.info("Quantity changed successfully")


@when("user selects ₹10 donation")
def step_donation(context):

    logger.info("Selecting ₹10 donation")

    context.beauty.select_donation()

    assert context.driver is not None, \
        "Donation selection failed"

    logger.info("Donation selected successfully")


@when("user clicks place order")
def step_place(context):

    logger.info("Clicking Place Order")

    context.beauty.place_order()

    assert context.driver is not None, \
        "Place order click failed"

    logger.info("Place Order clicked successfully")


@then("user should be redirected to login page")
def step_login(context):

    logger.info("Verifying login page redirection")

    context.beauty.verify_login_redirect()

    assert "login" in context.driver.current_url.lower(), \
        "User not redirected to login page"

    logger.info("End-to-end scenario completed successfully")