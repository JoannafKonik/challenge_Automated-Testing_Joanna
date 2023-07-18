import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.remind_password_page import RemindPasswordPage
from pages.base_page import BasePage


class TestRemindPassword(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        user_login.click_on_the_remind_password_button()
        remind_password_page = RemindPasswordPage(self.driver)
        remind_password_page.type_in_email('johnny@challenge.com')
        remind_password_page.click_on_send_button()
        remind_password_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()