import random
import unittest
from string import ascii_letters

import selenium.common.exceptions

from pages.cv_edit_page import CvEditPage
from pages.main_page import MainPage
from pages.tutorial_page import TutorialPage


class InterviewTests(unittest.TestCase):
    main_page = MainPage()
    tutorial_page = TutorialPage()
    cv_edit_page = CvEditPage()

    def test_register_link(self):
        # given
        random_last_name = ''.join(random.choices(ascii_letters, k=8))
        random_first_name = ''.join(random.choices(ascii_letters, k=12))

        # when
        self.main_page.go_to_page() \
            .click_register_link()
        self.tutorial_page.click_continue_link()
        self.cv_edit_page.insert_first_name(random_first_name) \
            .insert_last_name(random_last_name)

        # then
        displayed_credentials = self.cv_edit_page.get_first_and_last_name_displayed_on_preview()
        self.assertEqual(random_first_name + " " + random_last_name,
                         displayed_credentials)

        # when
        self.cv_edit_page.import_photo()

        # then
        try:
            self.cv_edit_page.expect_photo_uploaded_photo_displayed()
        except selenium.common.exceptions.TimeoutException:
            self.fail("Photo has not been uploaded correctly")


if __name__ == '__main__':
    unittest.main()
