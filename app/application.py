from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.products_page import ProductsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.products_page = ProductsPage(driver)