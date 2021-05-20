from os import getcwd
from time import sleep

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CvEditPage(BasePage):
    LAST_NAME_INPUT = (By.XPATH, '//input[@name="lastName"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@name="firstName"]')
    CREDENTIALS_OUTPUT = (By.XPATH, '(//div[@class ="_1XYsq"])[1]')
    IMPORT_PHOTO_BUTTON = (By.CSS_SELECTOR, 'div._3Wvmd.default input')
    ACCEPT_PHOTO_BUTTON = (By.CSS_SELECTOR, 'button._2w5CA._1TdXo.iconDirection--null._2i2-u._29Jel')
    UPLOADED_PHOTO_MINIATURE = (By.CSS_SELECTOR, "img._25f67")

    def insert_last_name(self, text):
        self.get_element(self.LAST_NAME_INPUT).send_keys(text)
        return self

    def insert_first_name(self, text):
        self.get_element(self.FIRST_NAME_INPUT).send_keys(text)
        return self

    def get_first_and_last_name_displayed_on_preview(self):
        # Wait for data to be fully displayed
        sleep(1)
        return self.get_element(self.CREDENTIALS_OUTPUT).text

    def import_photo(self):
        add_photo_element = self.get_element(self.IMPORT_PHOTO_BUTTON)
        add_photo_element.send_keys(getcwd() + "\example_picture.png")
        self.get_element(self.ACCEPT_PHOTO_BUTTON).click()


    def expect_photo_uploaded_photo_displayed(self):
        self.get_element(self.UPLOADED_PHOTO_MINIATURE, 30)
