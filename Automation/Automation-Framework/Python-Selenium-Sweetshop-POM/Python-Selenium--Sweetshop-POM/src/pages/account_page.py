from .base_page import BasePage
from selenium.webdriver.common.by import By

from src.pages.home_page import HomePage


class AccountPage(BasePage):
    NUMBER_OF_ORDERS_PLACED = (By.ID, "accountOrderCount")
    PAST_TRANSACTIONS = (By.ID, "transactions")
    ACCOUNT_HEADER = (By.XPATH, "//h1[normalize-space()='Your Account']")
    HOME_LINK = (By.XPATH, "//a[contains(@class, 'navbar-brand)]")

    def num_orders_placed_shown(self):
        return int(self.find(self.NUMBER_OF_ORDERS_PLACED).text)

    def click_home_link(self):
        from .home_page import HomePage
        self.click(self.HOME_LINK)
        return HomePage(self.driver)

    @property
    def past_transactions_displayed(self):
        return self.find(self.PAST_TRANSACTIONS).is_displayed()

    @property
    def account_header_displayed(self):
        return self.find(self.ACCOUNT_HEADER).is_displayed()

