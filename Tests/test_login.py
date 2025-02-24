
import pytest
from Pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.order(1)
def test_login(browser, config):
    login_page = LoginPage(browser)
    login_page.login(config["email"], config["password"])

    # Wait for an element unique to the dashboard (modify selector if needed)
    dashboard_locator = browser.locator(".v-img__img.v-img__img--contain")
    expect(dashboard_locator).to_be_visible(timeout=5000)  # Wait for 5 seconds
    # assert dashboard_locator.is_visible()  # Check if the element is visible
    # assert dashboard_locator.is_enabled()  # Check if the element is enabled
    # print(f"Page title after login: {browser.title()}")


    assert "Rooya Fleet Portal" in browser.title()