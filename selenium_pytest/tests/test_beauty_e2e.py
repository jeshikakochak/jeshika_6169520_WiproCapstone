from pages.home_page import HomePage
from pages.beauty_page import BeautyPage
from pages.cart_page import CartPage
from utils.setup_logger import setup_logger

logger = setup_logger()


def test_beauty_end_to_end(driver):
    home = HomePage(driver)
    beauty = BeautyPage(driver)
    cart = CartPage(driver)

    home.open_homepage()

    # any product here
    home.search_product("concealer")

    beauty.select_first_product()
    beauty.switch_to_product_tab()
    beauty.select_size_if_available()
    beauty.add_to_bag()

    cart.open_cart()

    assert "cart" in driver.current_url.lower()