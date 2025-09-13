from allure_commons.types import AttachmentType
import allure
class Constants:
    def __init__(self):
        print("constants loaded")

    @staticmethod
    def app_url():
        return "https://beatskpltest.prowessbeat.net/"

    @staticmethod
    def app_dashboard_url():
        return "https://beatskpltest.prowessbeat.net/Home/Index?returnUrl=%2F#no-back-button"

    @staticmethod
    def take_screenshot(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)