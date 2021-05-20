from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium_variables import DRIVER, _deafult_implicit_wait


class BasePage:

    def __init__(self):
        self.driver = DRIVER

    def get_element(self, locator, max_wait=_deafult_implicit_wait):
        return WebDriverWait(self.driver, max_wait).until(expected_conditions.presence_of_element_located(locator))
