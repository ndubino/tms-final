import time

import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MembershipsPage(BasePage):
    PAGE_URL = Links.MEMBERSHIP_PAGE

    ADD_BUTTON = ("xpath", "//i[@class='oxd-icon bi-plus oxd-button-icon'][1]")
    MEMBERSHIP_DROPDOWN = ("xpath", "(//div[@class='oxd-select-wrapper'])[1]")
    SUBSCRIPTION_PAID_BY_DROPDOWN = ("xpath", "(//div[@class='oxd-select-wrapper'])[2]")
    SUBSCRIPTION_AMOUNT_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    SUBSCRIPTION_CURRENCY_DROPDOWN = ("xpath", "(//div[@class='oxd-select-wrapper'])[3]")
    SUBSCRIPTION_COMMENCE_DATE_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[3]")
    SAVE_BUTTON = ("xpath", "//button[text()=' Save ']")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    DELETE_BUTTON = ("xpath", "(//i[@class = 'oxd-icon bi-trash'])[1]")
    DELETE_CONFIRM_BUTTON = ("xpath", "//i[@class = 'oxd-icon bi-trash oxd-button-icon']")

    @allure.step("Click on 'Add' button")
    def click_add_membership_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    @allure.step("Set membership")
    def set_membership(self, membership):
        self.wait.until(EC.element_to_be_clickable(self.MEMBERSHIP_DROPDOWN)).click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@data-v-13cf171c and text()='{membership}']"))).click()

    @allure.step("Set subscription paid by")
    def set_subscription_paid_by(self, subscription_paid_by):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_PAID_BY_DROPDOWN)).click()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[@data-v-13cf171c and text()='{subscription_paid_by}']"))).click()

    @allure.step("Set subscription amount")
    def set_subscription_amount(self, subscription_amount):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_AMOUNT_FIELD)).send_keys(subscription_amount)

    @allure.step("Set subscription currency")
    def set_subscription_currency(self, subscription_currency):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_CURRENCY_DROPDOWN)).click()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[@data-v-13cf171c and text()='{subscription_currency}']"))).click()

    @allure.step("Set subscription commence date")
    def set_subscription_commence_date(self, subscription_commence_date):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_COMMENCE_DATE_FIELD)).send_keys(
            subscription_commence_date)

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Membership has been added successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

    @allure.step("Delete membership")
    def delete_membership(self):
        with allure.step("Delete membership"):
            self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()
            self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM_BUTTON)).click()
