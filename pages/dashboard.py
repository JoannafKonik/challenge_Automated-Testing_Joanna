import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    ScoutsPanel_label_xpath = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[text()='Sign out']"
    Futbol_Kolektyw_logo_xpath = "//*[@title='Logo Scouts Panel']"
    player_match_report_panel_xpath = "//p[contains(@class, 'MuiTypography-root MuiTypography-body2 MuiTypography-colorTextSecondary')]"
    dev_team_contact_label_xpath = "//*[text()='Dev team contact']"
    Shortcuts_heading_xpath = "//*[text()='Shortcuts']"
    add_player_button_xpath = "//*[text()='Add player']"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.Futbol_Kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
    def click_on_sign_out_button(self):
         self.click_on_the_element(self.sign_out_button_xpath)
