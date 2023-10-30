import time
from constants import DEFAULT_BROWSER, WEBSITE_URL
from pages.login_page import LoginPage
from utilities.driver_factory import get_driver
from utilities.logger import log
from utilities.waiters import wait_for_element_to_be_visible
from selenium.webdriver.common.by import By


APP_NAME = "Login Test"


def run_login_tests():
    log(f"Initiated", app_name=APP_NAME)

    try:
        driver = get_driver(DEFAULT_BROWSER)
        driver.get(WEBSITE_URL)
        log("Successfully accessed the login page.", app_name=APP_NAME)

        login_page = LoginPage(driver)
        login_page.set_username("testuser")
        login_page.set_password("password123")

        login_page.click_login()
        log("Login attempt made, awaiting response...", app_name=APP_NAME)

        transactions_table = wait_for_element_to_be_visible(
            driver, (By.CLASS_NAME, "element-box-tp")
        )
        assert transactions_table != None, "Login failed: transactions table not loaded."
        log("Login successful, transactions table has loaded", app_name=APP_NAME)
        return True

    except AssertionError as e:
        log(f"AssertionError: {e}", "ERROR", app_name=APP_NAME)
        return False

    except Exception as e:
        log(f"Unexpected error: {e}", "ERROR", app_name=APP_NAME)
        return False

    finally:
        log(f"Completed.", app_name=APP_NAME)
        driver.quit()
