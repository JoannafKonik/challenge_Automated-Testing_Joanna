import time

from pages.base_page import BasePage

class RemindPasswordPage(BasePage):
    email_field_xpath = "//*[@name='email']"
    send_button_xpath = "//*[@type='submit']"
    snackbar_xpath = "//*[contains(@class, 'Toastify__toast-container Toastify__toast-container--top-right')]"
    remind_password_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'
    expected_title = 'Remind password'


    def type_in_email(self,email):
        self.field_send_keys(self.email_field_xpath, email)
    def click_on_send_button(self):
        self.click_on_the_element(self.send_button_xpath)
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.snackbar_xpath)
        assert self.get_page_title(self.remind_password_url) == self.expected_title
    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.remind_password_url) == self.expected_title
