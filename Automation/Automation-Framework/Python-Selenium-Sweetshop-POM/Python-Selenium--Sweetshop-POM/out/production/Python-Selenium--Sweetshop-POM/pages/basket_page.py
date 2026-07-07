from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    FIRST_NAME_FIELD = (By.XPATH, " //label[normalize-space()='First name']/following-sibling::input")
    LAST_NAME_FIELD = (By.XPATH, "//label[normalize-space()='Last name']/following-sibling::input")
    EMAIL_FIELD = (By.ID, "email")
    ADDRESS_FIELD = (By.ID, "address")
    ADDRESS_2_FIELD = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    CITY_DROPDOWN = (By.ID, "city")
    ZIP_FIELD = (By.ID, "zip")
    CARD_NAME_FIELD = (By.ID, "cc-name")
    CARD_NUM_FIELD = (By.ID, "cc-number")
    EXP_DATE_FIELD = (By.ID, "cc-expiration")
    CVV_FIELD = (By.ID, "cc-cvv")
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'checkout')]")
    RADIO_BUTTON_FREE_SHIPPING = (By.XPATH, "//label[@for='exampleRadios1']")
    RADIO_BUTTON_STANDARD_SHIPPING = (By.XPATH, "//label[@for='exampleRadios2']")
    EMPTY_BASKET_LINK = (By.XPATH, "//a[@href='#']")
    BASKET_HEADER = (By.XPATH, "//h1[normalize-space()='Your Basket']")
    YOUR_BASKET = (By.XPATH, "//ul[@id='basketItems']")

    # ERRORS
    FIRST_NAME_ERROR = (By.XPATH, "//div[normalize-space()='Valid first name is required.']")
    LAST_NAME_ERROR = (By.XPATH, "//div[normalize-space()='Valid last name is required.']")
    EMAIL_ERROR = (By.XPATH, "//div[normalize-space()='Please enter a valid email address for shipping updates.']")
    ADDRESS_ERROR = (By.XPATH, "//div[normalize-space()='Please enter your shipping address.']")
    COUNTRY_ERROR = (By.XPATH, "//div[normalize-space()='Please select a valid country.']")
    CITY_ERROR = (By.XPATH, "//div[normalize-space()='Please provide a valid state.']")
    ZIP_ERROR = (By.XPATH, "//div[normalize-space()='Zip code required.']")
    CARD_NAME_ERROR = (By.XPATH, "//div[normalize-space()='Name on card is required']")
    CARD_NUM_ERROR = (By.XPATH, "//div[normalize-space()='Credit card number is required']")
    EXP_DATE_ERROR = (By.XPATH, "//div[normalize-space()='Expiration date required']")
    CVV_ERROR = (By.XPATH, "//div[normalize-space()='Security code required']")

    def set_first_name(self, first_name):
        self.set(self.FIRST_NAME_FIELD, first_name)
        return first_name

    def set_last_name(self, last_name):
        self.set(self.LAST_NAME_FIELD, last_name)
        return last_name

    def set_email(self, email):
        self.set(self.EMAIL_FIELD, email)
        return email

    def set_address1(self, address):
        self.set(self.ADDRESS_FIELD, address)
        return address

    def set_address2(self, address2):
        self.set(self.ADDRESS_2_FIELD, address2)
        return address2

    def set_country(self, country):
        self.select_by_text(self.COUNTRY_DROPDOWN, country)

    def set_city(self, city):
        self.select_by_text(self.CITY_DROPDOWN, city)

    def set_zip(self, zip_code):
        self.set(self.ZIP_FIELD, zip_code)

    def set_card_name(self, card_name):
        self.set(self.CARD_NAME_FIELD, card_name)

    def set_card_num(self, card_num):
        self.set(self.CARD_NUM_FIELD, card_num)

    def set_exp_date(self, exp_date):
        self.set(self.EXP_DATE_FIELD, exp_date)

    def set_cvv(self, cvv):
        self.set(self.CVV_FIELD, cvv)

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)

    def click_free_shipping(self):
        self.click(self.RADIO_BUTTON_FREE_SHIPPING)

    def click_standard_shipping(self):
        self.click(self.RADIO_BUTTON_STANDARD_SHIPPING)

    def clear_basket(self):
        self.click(self.EMPTY_BASKET_LINK)

    def get_first_name_value(self):
        return self.find(self.FIRST_NAME_FIELD).get_attribute("value")

    def get_last_name_value(self):
        return self.find(self.LAST_NAME_FIELD).get_attribute("value")

    def get_email_value(self):
        return self.find(self.EMAIL_FIELD).get_attribute("value")

    def get_address1_value(self):
        return self.find(self.ADDRESS_FIELD).get_attribute("value")

    def get_address2_value(self):
        return self.find(self.ADDRESS_2_FIELD).get_attribute("value")

    def get_zip_value(self):
        return self.find(self.ZIP_FIELD).get_attribute("value")

    def get_card_name_value(self):
        return self.find(self.CARD_NAME_FIELD).get_attribute("value")

    def get_card_number_value(self):
        return self.find(self.CARD_NUM_FIELD).get_attribute("value")

    def get_exp_date_value(self):
        return self.find(self.EXP_DATE_FIELD).get_attribute("value")

    def get_cvv_value(self):
        return self.find(self.CVV_FIELD).get_attribute("value")


    def basket_header_displayed(self):
        return self.find(self.BASKET_HEADER).is_displayed()

    def get_first_name_error(self):
        return self.find(self.FIRST_NAME_ERROR).text

    def get_last_name_error(self):
        return self.find(self.LAST_NAME_ERROR).text

    def get_email_error(self):
        return self.find(self.EMAIL_ERROR).text

    def get_address_error(self):
        return self.find(self.ADDRESS_ERROR).text

    def get_country_error(self):
        return self.find(self.COUNTRY_ERROR).text

    def get_city_error(self):
        return self.find(self.CITY_ERROR).text

    def get_zip_error(self):
        return self.find(self.ZIP_ERROR).text

    def get_card_name_error(self):
        return self.find(self.CARD_NAME_ERROR).text

    def get_card_num_error(self):
        return self.find(self.CARD_NUM_ERROR).text

    def get_exp_date_error(self):
        return self.find(self.EXP_DATE_ERROR).text

    def get_cvv_error(self):
        return self.find(self.CVV_ERROR).text

    def is_product_in_basket(self, product_name):
        return any(
            product_name in item.text
            for item in self.find_all(self.YOUR_BASKET)
        )


    def complete_checkout(self, data):
        self.set_first_name(data.first_name)
        self.set_last_name(data.last_name)
        self.set_email(data.email)
        self.set_address1(data.address1)

        if data.address2:
            self.set_address2(data.address2)

        self.set_country(data.country)
        self.set_city(data.city)
        self.set_zip(data.zip)
        self.set_card_name(data.cc_name)
        self.set_card_num(data.cc_number)
        self.set_exp_date(data.exp_date)
        self.set_cvv(data.cvv)
        self.click_standard_shipping()
        self.click_checkout_button()

    @property
    def checkout_form_is_cleared(self):
        fields = [
            self.get_first_name_value(),
            self.get_last_name_value(),
            self.get_email_value(),
            self.get_address1_value(),
            self.get_address2_value(),
            self.get_zip_value(),
            self.get_card_name_value(),
            self.get_card_number_value(),
            self.get_exp_date_value(),
            self.get_cvv_value(),
        ]
        return all(not (field or "").strip() for field in fields)



