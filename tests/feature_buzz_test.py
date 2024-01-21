# Tests for Buzz functionality
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Buzz Functionality")
class TestNewsfeedFeature(BaseTest):
    @allure.title("Post a buzz")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_make_a_post(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_buzz_link()
        self.buzz_page.is_opened()
        self.buzz_page.post_buzz()
        self.buzz_page.click_post_button()
        self.buzz_page.is_changes_saved()
        self.buzz_page.make_screenshot("Success")

    @allure.title("Delete a buzz")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_delete_a_post(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_buzz_link()
        self.buzz_page.is_opened()
        self.buzz_page.delete_buzz()
        self.buzz_page.is_changes_saved()
        self.buzz_page.make_screenshot("Success")
