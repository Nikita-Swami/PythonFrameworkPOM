import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Assertions and use the Page Object class

# Webdriver Start
# User Interaction + Assertions
# Close Webdriver

#from tests.constants.constants import Constants
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(usr="admin@admin.com", pwd="admin")
    time.sleep(5)
    error_msg_element = login_page.get_error_message_text()
    assert error_msg_element == "Your email, password, IP address or location did not match"

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(usr="contact+atb7x@thetestingacademy.com", pwd="Wingify@1234")
    time.sleep(10)
    dashboardPage = DashboardPage(driver=setup)
    assert "Aman Ji" in dashboardPage.user_logged_in_text()