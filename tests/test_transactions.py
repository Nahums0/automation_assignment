import time
from constants import DEFAULT_BROWSER, EXPECTED_COMPLETED_TRANSACTIONS, WEBSITE_URL
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.driver_factory import get_driver
from utilities.logger import log

APP_NAME = "Transaction Count Test"

def run_transaction_tests():
    log(f"Initiated", app_name=APP_NAME)

    try:
        driver = get_driver(DEFAULT_BROWSER)
        driver.get(WEBSITE_URL)
        log("Successfully accessed the login page.", app_name=APP_NAME)

        # Login process
        login_page = LoginPage(driver)
        login_page.set_username("testuser")
        login_page.set_password("password123")
        login_page.click_login()
        log("Login attempt made, awaiting transactions table...", app_name=APP_NAME)

        # Transactions table process
        transactions_page = DashboardPage(driver)
        successful_transactions = transactions_page.get_successful_transactions()
        count_successful_transactions = len(successful_transactions)

        expected_transactions = EXPECTED_COMPLETED_TRANSACTIONS
        assert (
            count_successful_transactions == expected_transactions
        ), f"Expected {expected_transactions} successful transactions but found {count_successful_transactions}."

        log(f"Found {count_successful_transactions} successful transactions as expected.", app_name=APP_NAME)
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
