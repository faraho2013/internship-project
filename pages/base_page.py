from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'Opening URL {url}')


    def get_current_url(self):
        return self.driver.current_url

    def click(self, *locator):
        logger.info(f'Clicking element by {locator}')
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def wait_for_element_to_be_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"The element by {locator} is not visible"
        )

    def wait_for_element_to_be_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"The element by {locator} is visible"
        )

    def wait_for_element_to_be_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"The element by {locator} is not clickable"
        )

    def wait_for_element_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"The element by {locator} is not clickable"
        ).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering text "{text}" by {locator}')
        self.driver.find_element(*locator).send_keys(text)