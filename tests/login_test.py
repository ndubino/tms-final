import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Login Functionality")
class TestLogin(BaseTest):
    @allure.title("Login to the system successfully")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_make_a_post(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.make_screenshot("Success")

    @allure.title("Login to the system with invalid credentials")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_delete_a_post(self):
        self.login_page.open()
        self.login_page.enter_login("invalid")
        self.login_page.enter_password("invalid")
        self.login_page.click_submit_button()
        self.login_page.is_opened()
        self.login_page.make_screenshot("Success")
