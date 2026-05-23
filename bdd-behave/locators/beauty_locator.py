from selenium.webdriver.common.by import By


class BeautyLocators:

    SEARCH_BOX = (
        By.CLASS_NAME,
        "desktop-searchBar"
    )

    BEAUTY_MENU = (
        By.XPATH,
        "//a[@data-group='beauty']"
    )

    PRODUCTS = (
        By.XPATH,
        "//li[contains(@class,'product-base')]//a"
    )

    SIZE = (
        By.XPATH,
        "(//div[contains(@class,'size-buttons-size-button') or contains(@class,'size-buttons-unified-size')])[1]"
    )

    ADD_TO_BAG = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    GO_TO_BAG = (
        By.XPATH,
        "//span[contains(text(),'GO TO BAG')]"
    )

    SEARCH_HEADING = (
        By.CLASS_NAME,
        "title-title"
    )

    CART_ITEM = (
        By.CLASS_NAME,
        "itemContainer-base-item"
    )

    QUANTITY_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'itemComponents-base-quantity')]"
    )

    QUANTITY_TWO = (
        By.XPATH,
        "(//div[contains(@class,'dialogs-base-item')])[2]"
    )

    DONATION = (
        By.XPATH,
        "//div[contains(.,'₹10')]"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//button[contains(.,'PLACE ORDER')]"
    )

    POPUP_CLOSE = (
        By.XPATH,
        "//span[contains(@class,'desktop-iconClose')]"
    )

    PDP_TITLE = (
        By.CLASS_NAME,
        "pdp-title"
    )