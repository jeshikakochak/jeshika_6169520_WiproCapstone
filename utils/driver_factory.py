
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


from webdriver_manager.chrome import ChromeDriverManager

def get_driver():

    options = webdriver.ChromeOptions()


    # Add browser argument
    # "--start-maximized":opens browser in full screen/maximized mode
    # Without this:
    # browser opens in small default size
    options.add_argument("--start-maximized")



    # Create Chrome browser instance
    # webdriver.Chrome() launches Chrome browser
    # service=
    # tells Selenium which ChromeDriver executable to use
    # ChromeDriverManager().install()
    # automatically downloads correct ChromeDriver
    # options=
    # applies browser settings created above
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )



    # Implicit wait
    # Selenium waits up to 10 seconds while finding elements
    # Example:if search box loads after 5 seconds,
    # Selenium waits instead of failing immediately
    # Applies globally to all find_element() calls
    driver.implicitly_wait(10)



    # Return browser object
    # This allows other files to use the browser
    # Example:driver = get_driver()
    return driver