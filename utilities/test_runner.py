import concurrent.futures
from utilities.logger import log

def run_tests(tests_list, parallel_workers_count = 2):
    successful_tests_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=parallel_workers_count) as executor:
        futures = [executor.submit(test_func) for test_func in tests_list]

    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            if result is True:
                successful_tests_count += 1
        except Exception as e:
            log(f"An error occurred during test execution: {e}", "ERROR")

    return successful_tests_count
