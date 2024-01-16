from datetime import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class NewsfeedPage(BasePage):

        PAGE_URL = Links.NEWSFEED_PAGE

        POST_TEXT_FIELD = ("xpath", "//*[@class='oxd-buzz-post-input']")
        POST_BUTTON = ("xpath", "//button[@type='submit']")
        SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

        def enter_post_text(self, post_text):
            with allure.step(f"Enter text: '{post_text}'"):
                post_text_field = self.wait.until(EC.element_to_be_clickable(self.POST_TEXT_FIELD))
                post_text_field.send_keys(post_text)
                self.text = post_text

        @allure.step("Changes has been saved successfully")
        def is_changes_saved(self):
                self.wait.until(EC.invisibility_of_element_located(self.SPINNER))







