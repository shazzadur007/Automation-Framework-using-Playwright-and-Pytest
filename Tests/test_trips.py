from playwright.sync_api._generated import Page
import pytest
from Pages.trips_page import TripsPage

@pytest.mark.order(3)
def test_trips(browser,login):
    trips_page = TripsPage(browser)
    trips_page.open_trips_page()
    trips_page.all_trips_tab()
    trips_page.search_trip("861778060607602")


