import sys
from pathlib import Path
import os

parents_path = Path(__file__).parents
project_root = os.path.abspath(parents_path[2])
sys.path.append(project_root)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from SessionSeven.Pages.Login import Login
from SessionSeven.Pages.MainPage import MainPage
import unittest


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(1)

    def test2(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("Admin")
        login.enter_password("admin1234")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()