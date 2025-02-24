from playwright.sync_api._generated import Page
import pytest
from Pages.devices_page import DevicesPage

@pytest.mark.order(4)

def test_device_status_api(browser, login): 
    """Test to find which API fetches device status and verify device status."""
    devices_page = DevicesPage(browser)

    # Intercept API calls to capture the API that fetches device status
    def capture_api_call(route):
        response = route.continue_()
        request_url = route.request.url
        if "device" in request_url.lower(): 
            print(f"🔹 API Called: {request_url}")
            print(f"🔹 Response: {route.request.post_data_json}")

    # Monitor all network requests for devices
    browser.route("**/*", capture_api_call)

    # Open devices page and wait for the device list to load
    devices_page.open_devices_page()

    # Get the device status for a specific device
    device_id = "861778060607602"
    status = devices_page.get_device_status(device_id)
    print(f"Device Status for {device_id}: {status}")

