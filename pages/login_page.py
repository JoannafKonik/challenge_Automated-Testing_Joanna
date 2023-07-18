import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    ScoutsPanel_label_xpath = "//*[text()='Scouts Panel']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    language_select_listbox_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    login_label_xpath = "//*[@id='login-label']"
    password_label_xpath = "//*[@id='password-label']"
    sign_in_label_xpath = "//*[contains(@class, 'MuiButton-label')]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = 'Scouts panel - sign in'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_signin_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title
    def click_on_the_remind_password_button(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)
