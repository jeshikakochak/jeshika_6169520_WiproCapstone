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


@when("user closes popup if present")
def step_popup(context):
    context.home.close_popup_if_present()


@when("user hovers over beauty menu")
def step_hover(context):
    context.home.hover_beauty_menu()


@when('user selects "Lip Balm" category')
def step_category(context):
    context.home.select_category("Lip Balm")


@when("user opens first product")
def step_product(context):
    context.beauty = BeautyPage(context.driver)
    context.beauty.open_first_product()


@when("user switches to product tab")
def step_switch(context):
    context.beauty.switch_tab()


@when("user selects size if available")
def step_size(context):
    context.beauty.select_size()


@when("user adds product to bag")
def step_add(context):
    context.beauty.add_to_bag()


@when("user goes to shopping bag")
def step_bag(context):
    context.beauty.go_to_bag()


@when("user verifies cart item")
def step_cart(context):
    context.beauty.verify_cart()


@when("user changes quantity to 2")
def step_quantity(context):
    context.beauty.change_quantity()


@when("user selects ₹10 donation")
def step_donation(context):
    context.beauty.select_donation()


@when("user clicks place order")
def step_place(context):
    context.beauty.place_order()


@then("user should be redirected to login page")
def step_login(context):
    context.beauty.verify_login_redirect()