import os
import time
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddPlayer

class TestAddNewPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player_submit(self):
        user_Login = LoginPage(self.driver)
        user_Login.type_in_email('user09@getnada.com')
        user_Login.type_in_password('Test-1234')
        user_Login.click_on_the_signin_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.type_in_email('johnny@challenge.com')
        add_a_player_page.type_in_name('Johnny')
        add_a_player_page.type_in_surname('TheBest')
        add_a_player_page.type_in_phone('909707505')
        add_a_player_page.type_in_weight('189')
        add_a_player_page.type_in_height('83')
        add_a_player_page.type_in_age('15112001')
        add_a_player_page.click_on_the_leg_button()
        add_a_player_page.click_on_the_left_leg()
        add_a_player_page.type_in_club('Manchester')
        add_a_player_page.type_in_level('Advance')
        add_a_player_page.type_in_main_position('Goalkeeper')
        add_a_player_page.type_in_second_position('Defender')
        add_a_player_page.click_on_district_button()
        add_a_player_page.click_on_name_district()
        add_a_player_page.type_in_achievements('World Champion')
        add_a_player_page.click_on_add_language_button()
        add_a_player_page.type_in_first_languages('English')
        add_a_player_page.click_on_the_submit_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()


class TestAddNewPlayer_clear_form(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player_clear(self):
        user_Login = LoginPage(self.driver)
        user_Login.type_in_email('user09@getnada.com')
        user_Login.type_in_password('Test-1234')
        user_Login.click_on_the_signin_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.type_in_email('johnny@challenge.com')
        add_a_player_page.type_in_name('Johnny')
        add_a_player_page.type_in_surname('TheBest')
        add_a_player_page.type_in_phone('909707505')
        add_a_player_page.type_in_weight('189')
        add_a_player_page.type_in_height('83')
        add_a_player_page.type_in_age('15112001')
        add_a_player_page.click_on_the_leg_button()
        add_a_player_page.click_on_the_right_leg()
        add_a_player_page.type_in_club('Manchester')
        add_a_player_page.type_in_level('Advance')
        add_a_player_page.type_in_main_position('Goalkeeper')
        add_a_player_page.type_in_second_position('Defender')
        add_a_player_page.click_on_district_button()
        add_a_player_page.click_on_name_district()
        add_a_player_page.type_in_achievements('World Champion')
        add_a_player_page.click_on_add_language_button()
        add_a_player_page.type_in_first_languages('English')
        add_a_player_page.click_on_add_language_button()
        add_a_player_page.type_in_second_languages('Japanese')
        add_a_player_page.click_on_the_clear_button()
        add_a_player_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()