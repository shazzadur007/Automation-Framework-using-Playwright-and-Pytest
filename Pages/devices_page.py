from Pages.base_page import BasePage

class DevicesPage(BasePage):
    DEVICE_STATUS = "span:has-text('861778060607602')" 
    Home_Page ="//div[contains(text(),'Home')]"
    def open_devices_page(self):
        """Navigate to the Devices page and wait for the device list to load."""
        self.click_element(self.Home_Page)
        # self.page.pause()
        

    def get_device_status(self, device_id):
        device_locator = f"span:has-text('861778060607602')"  
        self.page.wait_for_timeout(10000)
        return self.get_text(device_locator)

       