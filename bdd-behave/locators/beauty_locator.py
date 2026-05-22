from selenium.webdriver.common.by import By


class BeautyLocators:

    BEAUTY_MENU = (
        By.XPATH,
        "//a[@data-group='beauty']"
    )

    LIP_BALM = (
        By.XPATH,
        "//a[text()='Lip Balm']"
    )

    PRODUCT_LIST = (
        By.CLASS_NAME,
        "product-base"
    )

    PRODUCT_LINKS = (
        By.XPATH,
        "//li[contains(@class,'product-base')]//a"
    )

    PRODUCT_TITLE = (
        By.CLASS_NAME,
        "pdp-title"
    )

    SIZE_OPTION = (
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

    DONATION_10 = (
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