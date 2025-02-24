import email
from Pages.base_page import BasePage

class DriversPage(BasePage):
    Driver="//div[contains(text(),'Drivers')]"
    ADD_DRIVER_BUTTON = "#app > div > header > div.v-toolbar__extension > div > div > button"
    DRIVER_NAME_INPUT = "input[id*='input-'][placeholder$='Type here']"
    DRIVER_ID_INPUT = "input[id*='input-'][placeholder$='13234235']"
    modal="//div[@class='v-card-text pa-6 border-b-thin']"
    # input="input[id*='input-']"
    DRIVER_EMAIL_INPUT = "input[id*='input-'][placeholder$='Type here']"
    DRIVER_PHONE_INPUT = "input[id*='input-'][placeholder$='Type here']"
    SAVE_BUTTON = "button[class='v-btn v-btn--block v-btn--slim v-theme--light bg-secondary-500 v-btn--density-default v-btn--size-default v-btn--variant-flat pl-text-body rounded-lg pl-text-body rounded-lg flex-fill']"
    DRIVER_Name="Shazzad"
    DRIVER_Id="E-123"
    DRIVER_Email= "123@gmail.com"
    close_button = "div[class='v-col flex-grow-0'] span[class='v-btn__content']"

    def open_drivers_page(self):
        self.click_element(self.Driver)
        self.page.wait_for_selector(self.ADD_DRIVER_BUTTON, state="visible", timeout=5000)
        # self.page.pause()

    def add_driver(self):
        # self.page.wait_for_selector(self.ADD_DRIVER_BUTTON, state="visible", timeout=5000)
        self.click_element(self.ADD_DRIVER_BUTTON)
        # self.get_by_role("button", name="Add new driver").click()
        # Wait until the modal appears
        self.page.wait_for_selector(self.DRIVER_NAME_INPUT, state="visible", timeout=5000)
        modal_content = self.page.locator(self.modal)
        #Get the input field after waiting
        name_input = modal_content.locator(self.DRIVER_NAME_INPUT).first
        name_input.type(self.DRIVER_Name)
        id_input = modal_content.locator(self.DRIVER_ID_INPUT).first
        id_input.type(self.DRIVER_Id)
        email_input = modal_content.locator(self.DRIVER_EMAIL_INPUT).nth(1)
        email_input.type(self.DRIVER_Email)
        phone_input = modal_content.locator(self.DRIVER_PHONE_INPUT).nth(2)
        phone_input.type("01712345678")

    def save_driver(self):
        self.click_element(self.SAVE_BUTTON)
        # Wait until the modal disappears
        self.page.wait_for_selector(self.ADD_DRIVER_BUTTON, state="visible", timeout=5000)

        self.click_element(self.close_button)

