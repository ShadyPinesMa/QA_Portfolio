from .base_page import BasePage
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "exampleInputEmail")
    PASSWORD_FIELD = (By.ID, "exampleInputPassword")
    LOGIN_BUTTON = (By.ID, "btn_login")
    EMAIL_ERROR = (By.XPATH, "//div[@class='invalid-feedback invalid-email']")
    PASSWORD_ERROR = (By.XPATH, "//div[@class='invalid-feedback invalid-password']")
    HOME_PAGE_LINK = (By.XPATH, "//a[contains(@class, 'navbar-brand)]")
    LOGIN_HEADER = (By.XPATH, "//h1[normalize-space()='Login']")

    def set_email(self, email):
        self.set(self.EMAIL_FIELD, email)
        return self

    def set_password(self, password):
        self.set(self.PASSWORD_FIELD, password)
        return self

    def login_header_displayed(self):
        return self.find(self.LOGIN_HEADER).is_displayed()

    def click_login_button(self):
        from .account_page import AccountPage
        self.click(self.LOGIN_BUTTON)
        return AccountPage(self.driver)

    def login(self, email, password ):
        self.set_email(email)
        self.set_password(password)
        return self.click_login_button()

    def get_email_error_message(self):
        return self.find(self.EMAIL_ERROR).text

    def get_password_error_message(self):
        return self.find(self.PASSWORD_ERROR).text








