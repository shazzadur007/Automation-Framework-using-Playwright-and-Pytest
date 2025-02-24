from Pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = "#input-2"
    PASSWORD_INPUT = "#input-4"
    LOGIN_BUTTON = "button[type='submit']"

    def login(self, email, password):
        self.fill_input(self.EMAIL_INPUT, email)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
