from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from selenium_variables import _base_url


class MainPage(BasePage):
    BEGIN_LINK = (By.XPATH, '//div[@class="_2vCLG _3qPjW"]')

    def click_register_link(self):
        self.get_element(self.BEGIN_LINK, 30).click()

    def go_to_page(self):
        self.driver.get(_base_url)
        self.driver.maximize_window()
        return self
