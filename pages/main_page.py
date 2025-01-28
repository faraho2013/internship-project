from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class MainPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")
    # OFF_PLAN = (By.XPATH, "//*[text()='Off-plan']")
    OFF_PLAN = (By.CSS_SELECTOR, "[class*='menu-text-link-leaderboard w--current']")

    def open_main(self):
        self.open_url(' https://soft.reelly.io')
        sleep(5)

    def login(self, email, password):
        self.input_text(email, *self.EMAIL_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)
        self.click(*self.CONTINUE_BUTTON)
        sleep(5)

    def open_off_plan(self):
        self.click(*self.OFF_PLAN)
