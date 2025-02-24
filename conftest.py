import pytest
from playwright.sync_api import sync_playwright
import json

@pytest.fixture(scope="session")
def config():
    """Load configuration from config.json"""
    with open("config.json") as config_file:
        return json.load(config_file)

@pytest.fixture(scope="session")
def browser():
    """Launch Playwright browser and create a new page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")
        yield page
        # browser.close()


# Fixture for logging in to the application
@pytest.fixture(scope="session")
def login(browser, config):
    """Logs in to the application using pre-configured credentials"""
    # # Login details
    email = "yourmail@mail.com"
    password = "Testpassword123"
    
    # Navigate to login page
    page = browser
    page.goto("https://example.com")  # Adjust URL if needed
    
    # Enter credentials and submit the form
    page.fill("#input-2", email)
    page.fill("#input-4", password)
    page.click("button[type='submit']")
    
    # Wait for a successful login (dashboard element, adjust selector as needed)
    page.wait_for_selector(".v-img__img.v-img__img--contain")
    
    # Return the page for further interaction
    yield page

    # Cleanup after test
    # page.close()

