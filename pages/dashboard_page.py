import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    BUZZ_BUTTON = ("xpath", "//span[text()='Buzz']")
    DEPENDENTS_BUTTON = ("xpath", "//a[text()='Dependents']")
    MEMBERSHIP_BUTTON = ("xpath", "//a[text()='Memberships']")

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

    @allure.step("Click on 'Buzz' link")
    def click_buzz_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_BUTTON)).click()

    @allure.step("Click on 'Dependents' link")
    def click_dependents_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.DEPENDENTS_BUTTON)).click()

    @allure.step("Click on 'Membership' link")
    def click_membership_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.MEMBERSHIP_BUTTON)).click()