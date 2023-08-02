import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    addplayer_url = 'https://dareit.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'
    ScoutsPanel_label_xpath = "//*[text()='Scouts Panel']"
    Players_label_xpath = "//*[text()='Players']"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    age_field_xpath = "//*[@name='age']"
    leg_button_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    mainposition_field_xpath = "//*[@name='mainPosition']"
    secondposition_field_xpath = "//*[@name='secondPosition']"
    achievements_field_xpath = "//*[@name='achievements']"
    district_button_xpath = "//*[@id='mui-component-select-district']"
    name_district_xpath = "//*[@id='menu-district']/div[3]/ul/li[15]"
    add_languages_button = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[15]/button"
    first_languages_field_xpath = "//*[@name='languages[0]']"
    second_languages_field_xpath = "//*[@name='languages[1]']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
    required_field_xpath = "//*[@class='MuiFormHelperText-root Mui-error Mui-required']"


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.required_field_xpath)
        assert self.get_page_title(self.addplayer_url) == self.expected_title
    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
    def click_on_the_leg_button(self):
        self.click_on_the_element(self.leg_button_xpath)
    def click_on_the_left_leg(self):
        self.click_on_the_element(self.left_leg_xpath)
    def click_on_district_button(self):
        self.click_on_the_element(self.district_button_xpath)
    def click_on_name_district(self):
        self.click_on_the_element(self.name_district_xpath)
    def click_on_add_language_button(self):
        self.click_on_the_element(self.add_languages_button)
    def click_on_the_right_leg(self):
        self.click_on_the_element(self.right_leg_xpath)
    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)
    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)
    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)
    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)
    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)
    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)
    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)
    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)
    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)
    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)
    def type_in_main_position(self, mainposition):
        self.field_send_keys(self.mainposition_field_xpath, mainposition)
    def type_in_second_position(self, secondposition):
        self.field_send_keys(self.secondposition_field_xpath, secondposition)
    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)
    def type_in_first_languages(self, language):
        self.field_send_keys(self.first_languages_field_xpath, language)
    def type_in_second_languages(self, language):
        self.field_send_keys(self.second_languages_field_xpath, language)
