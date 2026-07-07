


def test_email_error_message(home_page):
    login_page = home_page.click_login_link()
    login_page.login(
        "abc123@email.com",
        "abc123"
    )
    actual_message = login_page.get_email_error_message()
    assert "demo email addresses" in actual_message

def test_password_error_message(home_page):
    login_page = home_page.click_login_link()
    login_page.set_email("oneorder@sweetshop.local")
    login_page.set_password("")
    login_page.click_login_button()
    actual_message = login_page.get_password_error_message()
    assert "Please enter a valid" in actual_message

