from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OffPlanPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "[class='project-name']")
    VISUALIZATION_OPTION = (By.CSS_SELECTOR, "[class*='tabs-menu-project w-tab-menu']")

    def open_first_off_plan_product(self):
        self.click(*self.FIRST_PRODUCT)

    def visualization_option_is_available(self):
        self.wait_for_element_to_be_visible(*self.VISUALIZATION_OPTION)