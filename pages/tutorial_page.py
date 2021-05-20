from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class TutorialPage(BasePage):
    CONTINUE_LINK = (By.LINK_TEXT, 'Pomiń')

    def click_continue_link(self):
        self.get_element(self.CONTINUE_LINK).click()
