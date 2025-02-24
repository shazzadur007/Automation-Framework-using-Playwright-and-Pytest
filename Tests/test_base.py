import pytest
from playwright.sync_api import sync_playwright
import json

@pytest.fixture(scope="session")
def config():
    with open("config.json") as config_file:
        return json.load(config_file)

@pytest.fixture(scope="function")
def browser(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(config["base_url"])
        yield page
        browser.close()
