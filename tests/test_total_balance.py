from constants import DEFAULT_BROWSER, EXPECTED_TOTAL_BALANCE_VALUE, WEBSITE_URL
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.driver_factory import get_driver
from utilities.logger import log


APP_NAME = "Total Balance Test"


def run_total_balance_test():
    log(f"Initiated", app_name=APP_NAME)

    try:
        driver = get_driver(DEFAULT_BROWSER)
        driver.get(WEBSITE_URL)
        log("Successfully accessed the login page.", app_name=APP_NAME)

        login_page = LoginPage(driver)
        login_page.set_username("testuser")
        login_page.set_password("password123")

        login_page.click_login()
        log("Login attempt made, awaiting transactions table...", app_name=APP_NAME)

        balance_page = DashboardPage(driver)
        balance_value = balance_page.get_balance_value()

        assert (
            balance_value == EXPECTED_TOTAL_BALANCE_VALUE
        ), f"Expected {EXPECTED_TOTAL_BALANCE_VALUE} total balance value but found {balance_value}."

        log(f"Found {balance_value} for balance value as expected.", app_name=APP_NAME)
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
