# Test Dependents Feature
import allure
import pytest
from base.base_test import BaseTest


class TestDependentsFeature(BaseTest):
    @allure.title("Add a dependent")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_add_a_dependent(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_dependents_link()
        self.dependents_page.is_opened()
        self.dependents_page.click_add_dependent_button()
        self.dependents_page.set_name("tms-final")
        self.dependents_page.set_relationship("Child")
        self.dependents_page.set_date_of_birth("2024-01-22")
        self.dependents_page.click_save_button()
        self.dependents_page.is_changes_saved()
        self.dependents_page.make_screenshot("Success")

    @allure.title("Delete a dependent")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_delete_a_dependent(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_dependents_link()
        self.dependents_page.is_opened()
        self.dependents_page.delete_dependent()
        self.dependents_page.is_changes_saved()
        self.dependents_page.make_screenshot("Success")

