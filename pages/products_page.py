from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    OPTIONS_NAME = (By.CSS_SELECTOR, "[class='tabs-menu-project w-tab-menu']")
    SELECTED_OPTION = (By.CSS_SELECTOR, "[class*='w-tab-menu'] [class*='w--current']")

    def verify_visualization_options_clickable(self):
        expected_options = ['Architecture', 'Interior', 'Lobby']

        options = self.driver.find_elements(*self.OPTIONS_NAME)
        for option in options:
            option.click()

            selected_option = self.driver.find_element(*self.SELECTED_OPTION).text  # 'Color\nBlack'
            print('Current option', selected_option)
            assert selected_option in expected_options, f'Selected {selected_option} was not in expected options: {expected_options}'
