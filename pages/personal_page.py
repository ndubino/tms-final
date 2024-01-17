import platform
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_first_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))

            os_name = platform.system().lower()
            select_all = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL
            first_name_field.send_keys(select_all + "a")
            first_name_field.send_keys(Keys.BACKSPACE)

            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def is_first_name_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

    def change_last_name(self, new_last_name):
        with allure.step(f"Change last name on '{new_last_name}'"):
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))

            os_name = platform.system().lower()
            select_all = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL
            last_name_field.send_keys(select_all + "a")
            last_name_field.send_keys(Keys.BACKSPACE)

            last_name_field.send_keys(new_last_name)
            self.last_name = new_last_name

    @allure.step("Changes has been saved successfully")
    def is_last_name_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, self.last_name))

