from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def set(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(str(value))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text, clear=True):
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def select_by_text(self, locator, text):
        Select(self.find(locator)).select_by_visible_text(text)
