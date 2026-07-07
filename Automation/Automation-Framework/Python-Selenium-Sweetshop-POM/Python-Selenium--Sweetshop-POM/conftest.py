import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.account_page import AccountPage

URL = "https://sweetshop.vivrichards.co.uk/"

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def products_page(driver):
    return ProductsPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def basket_page(driver):
    return BasketPage(driver)

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()