from behave import given, when, then
from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from selenium.webdriver.common.by import By


@when("user hovers over beauty menu")
def step_hover(context):
    context.home.hover_beauty_menu()


@when("user selects first product")
def step_select(context):
    context.beauty = BeautyPage(context.driver)
    context.beauty.select_first_product()


@when("user switches to product tab")
def step_switch(context):
    context.beauty.switch_tab()


@when("user selects size")
def step_size(context):
    context.beauty.select_size()


@when("user clicks add to bag")
def step_add(context):
    context.beauty.add_to_bag()


@then("product should be added successfully")
def step_validate(context):

    assert "GO TO BAG" in context.driver.page_source