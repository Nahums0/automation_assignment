import os
from tests.test_login import run_login_tests
from tests.test_total_balance import run_total_balance_test
from tests.test_transactions import run_transaction_tests
from utilities.logger import setup_logger, log
from utilities.driver_factory import close_all_drivers
from utilities.test_runner import run_tests
from constants import LOG_FILE_NAME, PARALLEL_WORKERS_COUNT

def main():
    TESTS = [
        run_login_tests,
        run_transaction_tests,
        run_total_balance_test
    ]
    setup_logger(LOG_FILE_NAME)

    try:
        log(f"Running the following tests: {', '.join(func.__name__ for func in TESTS)}")
        successful_tests_count = run_tests(TESTS, PARALLEL_WORKERS_COUNT)
        log(f"Finished running all tests ({successful_tests_count}/{len(TESTS)} successfull tests)")
    except Exception as e:
        log(f"An error occurred during test execution: {e}", "ERROR")
    finally:
        log(f"Cleaning up all web drivers")
        close_all_drivers()

if __name__ == "__main__":
    main()
