from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    CHOCOLATE_CUPS = (By.XPATH, "//*[@data-name='Chocolate Cups']")
    SHERBERT_DISKS = (By.XPATH, "//*[@data-name='Sherbet Discs']")
    BONBONS = (By.XPATH, "//*[@data-name='Strawberry Bon Bons']")
    JELLIES = (By.XPATH, "//*[@data-name='Jellies']")
    FRUIT_SALADS = (By.XPATH, "//*[@data-name='Fruit Salads']")
    WHAM_BARS = (By.XPATH, "//*[@data-name='Wham Bar']")
    CHOCOLATE_BEANS = (By.XPATH, "//*[@data-name='Chocolate Beans']")
    NERDS = (By.XPATH, "//*[@data-name='Nerds']")
    HOME_PAGE_LINK = (By.XPATH, "//a[contains(@class, 'navbar-brand)]")
    BASKET_LINK = (By.XPATH, "//a[@href='/basket']")
    NUM_ITEMS_IN_BASKET = (By.XPATH, "//span[contains(@class, 'badge-success')]")
    PRODUCTS_HEADER = (By.XPATH, "//h1[text()='Browse sweets']")

    def add_chocolate_cups(self):
        self.click(self.CHOCOLATE_CUPS)

    def add_sherbert_disks(self):
        self.click(self.SHERBERT_DISKS)

    def add_bonbons(self):
        self.click(self.BONBONS)

    def add_jellies(self):
        self.click(self.JELLIES)

    def add_fruit_salads(self):
        self.click(self.FRUIT_SALADS)

    def add_wham_bars(self):
        self.click(self.WHAM_BARS)

    def add_chocolate_beans(self):
        self.click(self.CHOCOLATE_BEANS)

    def add_nerds(self):
        self.click(self.NERDS)

    def click_home_link(self):
        from .home_page import HomePage
        self.click(self.HOME_PAGE_LINK)
        return HomePage(self.driver)

    def click_basket_link(self):
        from .basket_page import BasketPage
        self.click(self.BASKET_LINK)
        return BasketPage(self.driver)

    def add_default_products(self):
        self.add_wham_bars()
        self.add_nerds()
        self.add_chocolate_cups()
        self.add_fruit_salads()
        self.add_bonbons()
        self.add_jellies()
        self.add_sherbert_disks()
        self.add_chocolate_beans()

        return self

    def products_header_displayed(self):
        return self.find(self.PRODUCTS_HEADER).is_displayed()

    def get_num_items_in_basket(self):
        return self.find(self.NUM_ITEMS_IN_BASKET).get_attribute("value")