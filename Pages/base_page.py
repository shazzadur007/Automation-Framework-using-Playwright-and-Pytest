from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def click_element(self, locator):
        self.page.locator(locator).click()

    def fill_input(self, locator, text):
        self.page.locator(locator).fill(text)
