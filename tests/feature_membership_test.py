# Test for membership functionality
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Membership Functionality")
class TestMembershipsFeature(BaseTest):

    @allure.title("Add membership")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_membership(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_membership_link()
        self.membership_page.is_opened()
        self.membership_page.click_add_membership_button()
        self.membership_page.set_membership("ACCA")
        self.membership_page.set_subscription_paid_by("Company")
        self.membership_page.set_subscription_amount("1000")
        self.membership_page.set_subscription_currency("Fiji Dollar")
        self.membership_page.set_subscription_commence_date("2024-01-22")
        self.membership_page.click_save_button()
        self.membership_page.is_changes_saved()

    @allure.title("Delete membership")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_membership(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_membership_link()
        self.membership_page.is_opened()
        self.membership_page.delete_membership()
        self.membership_page.is_changes_saved()
