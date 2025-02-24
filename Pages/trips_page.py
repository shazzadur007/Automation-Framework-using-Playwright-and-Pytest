from Pages.base_page import BasePage

class TripsPage(BasePage):
    TRIPs_PAGE = "#v-list-group--id-Trips"
    # device_id = "861778060607602"
    # SEARCH_INPUT = "//input[@aria-label='Device ID']"
    AllTrips_Tab = "//div[contains(text(),'All trips')]"
    # SEARCH_INPUT = "label[class='v-label opacity-100 v-field-label']"
    SEARCH_INPUT = "input[id*='input-'][class*='v-field__input']"

    
    def open_trips_page(self):
        self.click_element(self.TRIPs_PAGE)
       
    
    def all_trips_tab(self):
        # self.wait_for_selector(self.AllTrips_Tab, timeout=5000)
        self.click_element(self.AllTrips_Tab)
        

    def search_trip(self, device_id):
        # Wait for the input to be visible and ready
        self.page.wait_for_selector(self.SEARCH_INPUT, state="visible")
        
        # Get the input field and ensure it's visible
        device_input = self.page.locator(self.SEARCH_INPUT).first
        
        # Make sure the element is visible and ready for interaction
        device_input.wait_for(state="visible")
        
        # Clear any existing value
        device_input.clear()
        
        # Click to focus and then type
        device_input.click()
        device_input.type(device_id)
        self.page.wait_for_timeout(10000)



        # self.page.pause()
