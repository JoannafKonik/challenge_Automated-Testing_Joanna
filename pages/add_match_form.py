from pages.base_page import BasePage


class AddMatchForm(BasePage):
    ScoutsPanel_label_xpath = "//h6[contains(@class, 'MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap')]"
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore'and@class='MuiInputBase-input MuiInput-input']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_radio_button_xpath = '//input[@type='radio'and@name='matchAtHome'and@value='true']"
    match_out_home_radio_button_xpath = '//input[@type='radio'and@name='matchAtHome'and@value='false']"
    submit_button_xpath = "//*[contains(@class, 'MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary')]"
    clear_button_xpath = "//*[contains(@class, 'MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary')]"
