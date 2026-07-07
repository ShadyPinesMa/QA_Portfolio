import pytest
from utils.csv_utils import load_checkout_data


def test_is_basket_header_displayed(home_page):
    basket_page = home_page.click_basket_link()
    assert basket_page.basket_header_displayed, ("Basket header is not displayed")

def test_does_basket_display_correct_items(home_page):
    products_page = home_page.click_browse_sweets_button()
    products_page.add_default_products()
    basket_page = products_page.click_basket_link()
    expected_products = [
        "Nerds",
        "Chocolate Cups",
        "Wham Bar",
        "Chocolate Beans",
        "Fruit Salads",
        "Bon Bons",
        "Jellies",
        "Sherbet Discs",
    ]
    for product in expected_products:
        assert basket_page.is_product_in_basket(product)

def test_error_message_customer_info(home_page):
    products_page = home_page.click_browse_sweets_button()
    products_page.add_default_products()
    basket_page = products_page.click_basket_link()
    basket_page.set_card_name("Cary Grant")
    basket_page.set_card_num("9099888855557777")
    basket_page.set_exp_date("08/30")
    basket_page.set_cvv("101")
    basket_page.click_checkout_button()
    first_name_error = basket_page.get_first_name_error()
    assert "Valid first name" in first_name_error
    last_name_error = basket_page.get_last_name_error()
    assert "Valid last name" in last_name_error
    email_error = basket_page.get_email_error()
    assert "valid email address" in email_error
    address_error = basket_page.get_address_error()
    assert "enter your shipping address" in address_error
    country_error = basket_page.get_country_error()
    assert "valid country" in country_error
    city_error = basket_page.get_city_error()
    assert "valid state" in city_error
    zip_code_error = basket_page.get_zip_error()
    assert "Zip code required" in zip_code_error

def test_error_message_credit_card_info(home_page):
    products_page = home_page.click_browse_sweets_button()
    products_page.add_default_products()
    basket_page = products_page.click_basket_link()
    basket_page.set_first_name("Alphonse")
    basket_page.set_last_name("Elric")
    basket_page.set_email("aelric@mail.com")
    basket_page.set_address1("555 Cherry St")
    basket_page.set_country("United Kingdom")
    basket_page.set_city("Cardiff")
    basket_page.set_zip("12345")
    basket_page.click_checkout_button()
    card_name_error = basket_page.get_card_name_error()
    assert "Name on card" in card_name_error
    card_number_error = basket_page.get_card_num_error()
    assert "Credit card number" in card_number_error
    exp_error = basket_page.get_exp_date_error()
    assert "Expiration date" in exp_error
    cvv_error = basket_page.get_cvv_error()
    assert "Security code" in cvv_error

TEST_DATA = load_checkout_data("test_data/checkout_data.csv")


@pytest.mark.parametrize("checkout_data", TEST_DATA)
def test_verify_checkout_process(home_page, checkout_data):

    products_page = home_page.click_browse_sweets_button()
    products_page.add_default_products()

    basket_page = products_page.click_basket_link()

    basket_page.complete_checkout(checkout_data)

    assert basket_page.checkout_form_is_cleared
