from selenium import webdriver
from utilities.logger import log

_active_drivers = []

def get_driver(browser_name="chrome"):
    """Create a new WebDriver instance and return it."""

    browser_name = browser_name.lower()
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    _active_drivers.append(driver)
    return driver

def close_all_drivers():
    """Close all active driver instances."""

    global _active_drivers
    for driver in _active_drivers:
        try:
            driver.quit()
        except Exception as e:
            log(f"Failed to close driver: {e}")
    _active_drivers = []
