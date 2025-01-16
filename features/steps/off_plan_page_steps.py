from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


OPTIONS_NAME = (By.CSS_SELECTOR, "[class='tabs-menu-project w-tab-menu']")
SELECTED_OPTION = (By.CSS_SELECTOR, "[class*='w-tab-menu'] [class*='w--current']")


@when('Click on first off plan product')
def open_first_off_plan_product(context):
    context.app.off_plan_page.open_first_off_plan_product()
    sleep(10)


@then('Verify one of the three options is available')
def visualization_option_is_available(context):
    context.app.off_plan_page.visualization_option_is_available()


@then('Verify the visualization options are clickable')
def visualization_option_is_clickable(context):
        expected_options = ['Architecture', 'Interior', 'Lobby']

        options = context.driver.find_elements(*OPTIONS_NAME)
        for option in options:
            option.click()

            selected_option = context.driver.find_element(*SELECTED_OPTION).text  # 'Color\nBlack'
            print('Current option', selected_option)
            assert selected_option in expected_options, f'Selected {selected_option} was not in expected options: {expected_options}'
