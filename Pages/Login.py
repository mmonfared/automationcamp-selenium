from Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('id', login_button_id).click()