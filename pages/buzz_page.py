import platform
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class BuzzPage(BasePage):
    PAGE_URL = Links.BUZZ_PAGE

    BUZZ_TEXT_FIELD = ("xpath", "//textarea[@class='oxd-buzz-post-input']")
    BUZZ_POST_BUTTON = ("xpath", "//*[@class='oxd-button oxd-button--medium oxd-button--main']")
    BUZZ_SETTING_BUTTON = ("xpath", "//*[@class='orangehrm-buzz-post-header-config'][1]")
    BUZZ_DELETE_BUTTON = ("xpath", "//*[text()='Delete Post']")
    BUZZ_ACCEPT_DELETE_BUTTON = ("xpath", "//*[@class='oxd-icon bi-trash oxd-button-icon']")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def post_buzz(self):
        with allure.step("Fill buzz text field and post it"):
            buzz_text_field = self.wait.until(EC.element_to_be_clickable(self.BUZZ_TEXT_FIELD))

            os_name = platform.system().lower()
            select_all = Keys.COMMAND if os_name == 'darwin' else Keys.CONTROL

            buzz_text_field.send_keys(select_all + "a")
            buzz_text_field.send_keys(Keys.BACKSPACE)

            buzz_text_field.send_keys("TEST BUZZ")

    @allure.step("Post has been created successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

    @allure.step("Click on 'Post' button")
    def click_post_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_POST_BUTTON)).click()

    def delete_buzz(self):
        with allure.step("Delete buzz"):
            buzz_setting_button = self.wait.until(EC.element_to_be_clickable(self.BUZZ_SETTING_BUTTON))
            buzz_setting_button.click()
            self.wait.until(EC.element_to_be_clickable(self.BUZZ_DELETE_BUTTON)).click()
            self.wait.until(EC.element_to_be_clickable(self.BUZZ_ACCEPT_DELETE_BUTTON)).click()

    @allure.step("Buzz has been deleted successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
