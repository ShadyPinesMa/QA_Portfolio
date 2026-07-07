from conftest import home_page


def test_products_header_displayed(home_page):
    products_page = home_page.click_browse_sweets_button()
    assert products_page.products_header_displayed

def test_add_products_to_basket_positive(home_page):
    products_page = home_page.click_browse_sweets_button()
    products_page.add_nerds()
    products_page.add_wham_bars()
    products_page.add_fruit_salads()
    products_page.add_chocolate_cups()
    actual = products_page.get_num_items_in_basket()
    expected = 4
    assert actual == expected

def test_basket_link(home_page):
    products_page = home_page.click_browse_sweets_button()
    basket_page = products_page.click_basket_link()
    assert basket_page.basket_header_displayed, "Basket header is not displayed"

