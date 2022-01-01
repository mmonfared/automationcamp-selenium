from Locators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element('id', dashboard_label_id)
