from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//input[@name='login'and@type='text']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    ScoutsPanel_label_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography')]"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    language_select_listbox_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    login_label_xpath = "//*[@id='login-label']"
    password_label_xpath = "//*[@id='password-label']"
    sign_in_label_xpath = "//*[contains(@class, 'MuiButton-label')]"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
