import os
import time
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestSignOut(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out(self):
        user_Login = LoginPage(self.driver)
        user_Login.type_in_email('user09@getnada.com')
        user_Login.type_in_password('Test-1234')
        user_Login.click_on_the_signin_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_sign_out_button()
        user_Login = LoginPage(self.driver)
        user_Login.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
