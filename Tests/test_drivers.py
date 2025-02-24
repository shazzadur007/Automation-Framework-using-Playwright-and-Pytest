from playwright.sync_api._generated import Page
import pytest
from Pages.drivers_page import DriversPage

@pytest.mark.order(2)
def test_add_driver(browser,login):
    drivers_page = DriversPage(browser)
    drivers_page.open_drivers_page()
    drivers_page.add_driver()
    drivers_page.save_driver()

