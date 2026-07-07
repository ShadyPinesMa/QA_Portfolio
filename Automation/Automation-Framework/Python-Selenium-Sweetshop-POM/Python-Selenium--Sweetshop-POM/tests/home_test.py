

def test_go_to_products_page(home_page):
    products_page = home_page.click_browse_sweets_button()
    assert products_page.products_header_displayed, ("Products Header is not displayed.")

def test_go_to_login_page(home_page):
    login_page = home_page.click_login_link()
    assert login_page.login_header_displayed, ("Login Header is not displayed.")

def test_home_page_header(home_page):
    home_page.home_header_displayed()
    assert home_page.home_header_displayed, ("Home Header is not displayed")