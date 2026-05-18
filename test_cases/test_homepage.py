def test_myntra_homepage_open(driver):

    # Open Myntra website
    driver.get("https://www.myntra.com")

    # Validate homepage opened successfully
    assert "myntra" in driver.current_url.lower()