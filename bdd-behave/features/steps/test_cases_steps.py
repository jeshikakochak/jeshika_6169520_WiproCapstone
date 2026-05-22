from behave import given, when, then
from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from selenium.webdriver.common.by import By


@given("user opens Myntra homepage")
def step_open_home(context):
    context.home = HomePage(context.driver)
    context.home.open_homepage("https://www.myntra.com")


@when("user searches for invalid product")
def step_invalid_search(context):
    context.home.search_product("xyzlipbalm999")


@then("invalid search results should be displayed")
def step_validate_invalid(context):

    heading = context.driver.find_element(
        By.CLASS_NAME,
        "title-title"
    )

    assert "xyzlipbalm999" in heading.text.lower()


@given("user opens product page")
def step_open_product(context):

    context.driver.get(
        "https://www.myntra.com/serum-and-gel/minimalist/minimalist-vitamin-c-10-face-serum-for-glowing-skin-30-ml/14173102/buy"
    )


@when("user clicks add to bag without selecting size")
def step_negative_size(context):

    beauty = BeautyPage(context.driver)
    beauty.add_to_bag()


@then("product should not be added")
def step_validate_negative(context):

    assert "GO TO BAG" not in context.driver.page_source