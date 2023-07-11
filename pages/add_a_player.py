import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    addplayer_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.addplayer_url) == self.expected_title


