# Login Page Class

# Page Locators
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Skipper.utilsSkipper.common_utils import webdriver_wait
#from Skipper.pageObjectsSkipper.
#from selenium.webdriver import Chrome

#browser = Chrome()

class LoginPageSkipper:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "UserName")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//span[@class='field-validation-error']")


    #remember_checkbox = (By.XPATH, "//input[@id='RememberMe']")
    #forgot_password_button = (By.XPATH, "//a[@class='forgot-password-link']")

    # Page Actions

    def get_username(self):
        return self.driver.find_element(*LoginPageSkipper.username)

    def get_password(self):
        return self.driver.find_element(*LoginPageSkipper.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPageSkipper.login_button)

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username, timeout=5)
        return self.driver.find_element(*LoginPageSkipper.error_message)

    def login_to_skipper(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)


    def get_error_message_text(self):
        return self.get_error_message().text
             #pass


