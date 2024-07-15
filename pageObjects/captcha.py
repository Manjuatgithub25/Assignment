from utilities.locators import Locators


class CaptchaPage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def input_captcha(self, captcha):
        self.driver.find_element(*self.input).send_keys(captcha)

    def submit_captcha(self):
        self.driver.find_element(*self.submit).click()
