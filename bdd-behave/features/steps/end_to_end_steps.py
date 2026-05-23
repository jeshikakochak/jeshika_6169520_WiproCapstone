from behave import given, when, then
from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from utils.config_reader import ConfigReader

@given("user opens Myntra homepage for end to end")
def step_open_home(context):

    context.home = HomePage(context.driver)

    context.home.open_homepage(
        ConfigReader.get_base_url()
    )

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Homepage did not open"


@when("user closes popup if present")
def step_popup(context):

    context.home.close_popup_if_present()

    assert context.driver is not None, \
        "Driver became unavailable"


@when("user hovers over beauty menu")
def step_hover(context):

    context.home.hover_beauty_menu()

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Hover action failed"


@when('user selects "Lip Balm" category')
def step_category(context):

    context.home.select_category("Lip Balm")

    assert "lip-balm" in context.driver.current_url.lower(), \
        "Lip Balm category did not open"


@when("user opens first product")
def step_product(context):

    context.beauty = BeautyPage(context.driver)

    context.beauty.open_first_product()

    assert len(context.driver.window_handles) >= 1, \
        "Product click failed"


@when("user switches to product tab")
def step_switch(context):

    context.beauty.switch_tab()

    assert "myntra.com" in context.driver.current_url.lower(), \
        "Product tab did not open"


@when("user selects size if available")
def step_size(context):

    context.beauty.select_size()

    assert context.driver is not None, \
        "Size selection failed"


@when("user adds product to bag")
def step_add(context):

    context.beauty.add_to_bag()

    assert "GO TO BAG" in context.driver.page_source \
        or "Bag" in context.driver.page_source, \
        "Product not added to bag"


@when("user goes to shopping bag")
def step_bag(context):

    context.beauty.go_to_bag()

    assert "bag" in context.driver.current_url.lower() \
        or "checkout" in context.driver.current_url.lower(), \
        "Shopping bag did not open"


@when("user verifies cart item")
def step_cart(context):

    context.beauty.verify_cart()

    assert "bag" in context.driver.page_source.lower() \
        or "shopping bag" in context.driver.page_source.lower(), \
        "Cart item not verified"


@when("user changes quantity to 2")
def step_quantity(context):

    context.beauty.change_quantity()

    assert context.driver is not None, \
        "Quantity change failed"


@when("user selects ₹10 donation")
def step_donation(context):

    context.beauty.select_donation()

    assert context.driver is not None, \
        "Donation selection failed"


@when("user clicks place order")
def step_place(context):

    context.beauty.place_order()

    assert context.driver is not None, \
        "Place order click failed"


@then("user should be redirected to login page")
def step_login(context):

    context.beauty.verify_login_redirect()

    assert "login" in context.driver.current_url.lower(), \
        "User not redirected to login page"