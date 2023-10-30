from selenium.webdriver.common.by import By
from utilities.waiters import wait_for_element_to_be_visible

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def get_transactions_table(self):
        return wait_for_element_to_be_visible(self.driver, (By.CLASS_NAME, "table-responsive"))

    def get_all_transactions(self):
        table = self.get_transactions_table()
        return table.find_elements(By.TAG_NAME, "tr")

    def get_successful_transactions(self):
        transactions = self.get_all_transactions()
        return [row for row in transactions if "Complete" in row.text]

    def get_balance_value_element(self):
        return wait_for_element_to_be_visible(self.driver, (By.CLASS_NAME, "balance-value"))

    def get_balance_value(self):
        balance_value_element = self.get_balance_value_element()
        return balance_value_element.find_element(By.TAG_NAME, "span").text
