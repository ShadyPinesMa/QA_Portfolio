from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    BROWSE_SWEETS_BUTTON = (By.XPATH, "//a[@href='/sweets']")
    HOME_HEADER = (By.XPATH, "//h1[normalize-space()='Welcome to the sweet shop!']")
    BASKET_LINK = (By.XPATH, "//a[@href='/basket']")

    def click_login_link(self):
        from .login_page import LoginPage
        self.click(self.LOGIN_LINK)
        return LoginPage(self.driver)

    def click_browse_sweets_button(self):
        from .products_page import ProductsPage
        self.click(self.BROWSE_SWEETS_BUTTON)
        return ProductsPage(self.driver)


    def home_header_displayed(self):
        return self.find(self.HOME_HEADER).is_displayed()

    def click_basket_link(self):
        from .basket_page import BasketPage
        self.click(self.BASKET_LINK)
        return BasketPage(self.driver)

