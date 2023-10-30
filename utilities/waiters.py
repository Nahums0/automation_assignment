from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_to_be_visible(driver, by_locator, timeout=10):
    """Wait until the specified element is visible."""

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element
    except:
        return None
