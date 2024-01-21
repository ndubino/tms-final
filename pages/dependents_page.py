import platform
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# for inspect dropdown setTimeout(function() { debugger; }, 5000);

class DependentsPage(BasePage):
    PAGE_URL = Links.DEPENDENTS_PAGE

    ADD_DEPENDENT_BUTTON = ("xpath", "//i[@class='oxd-icon bi-plus oxd-button-icon'][1]")
    NAME_FIELD = ("xpath", "(//div[@data-v-2130bd2a]//input[@class='oxd-input oxd-input--active'])[1]")
    RELATIONSHIP_DROPDOWN = ("xpath", "//div[@class='oxd-select-wrapper']")
    DATA_OF_BIRTH_FIELD = ("xpath", "//input[@class='oxd-input oxd-input--active' and @placeholder='yyyy-mm-dd']")
    SAVE_BUTTON = ("xpath", "//button[text()=' Save ']")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    DELETE_BUTTON = ("xpath", "//i[@class = 'oxd-icon bi-trash'][1]")
    DELETE_CONFIRM_BUTTON = ("xpath", "//i[@class = 'oxd-icon bi-trash oxd-button-icon']")

    @allure.step("Click on 'Add Dependent' button")
    def click_add_dependent_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_DEPENDENT_BUTTON)).click()

    def set_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD))

            os_name = platform.system().lower()
            select_all = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL
            first_name_field.send_keys(select_all + "a")
            first_name_field.send_keys(Keys.BACKSPACE)

            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Set relationship")
    def set_relationship(self, relationship):
        self.wait.until(EC.element_to_be_clickable(self.RELATIONSHIP_DROPDOWN)).click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@data-v-13cf171c and text()='{relationship}']"))).click()

    @allure.step("Set date of birth")
    def set_date_of_birth(self, date_of_birth):
        self.wait.until(EC.element_to_be_clickable(self.DATA_OF_BIRTH_FIELD)).send_keys(date_of_birth)

    @allure.step("Click on 'Save' button")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Dependent has been added successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

    def delete_dependent(self):
        with allure.step("Delete dependent"):
            self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()
            self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM_BUTTON)).click()