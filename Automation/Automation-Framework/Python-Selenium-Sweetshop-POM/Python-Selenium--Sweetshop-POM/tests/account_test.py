


def test_account_header_displayed(home_page):
    login_page = home_page.click_login_link()
    login_page.set_email("oneorder@sweetshop.local")
    login_page.set_password("abc123")
    account_page = login_page.click_login_button()
    assert account_page.account_header_displayed

def test_number_of_orders_displayed(home_page):
    login_page = home_page.click_login_link()
    account_page = login_page.login(
        "fiveorders@sweetshop.local",
        "abc123"
    )
    actual = account_page.num_orders_placed_shown()
    expected = 5
    assert actual == expected

def test_past_transactions_displayed(home_page):
    login_page = home_page.click_login_link()
    account_page = login_page.login(
        "twoorders@sweetshop.local",
        "abc123"
    )
    assert account_page.past_transactions_displayed

