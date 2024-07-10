from selenium.webdriver.common.by import By


class CaptchaPage:

    def __init__(self, driver):
        self.driver = driver

    input = (By.ID, "captchacharacters")
    submit = (By.XPATH, "//button[@type='submit']")

    def input_captcha(self, captcha):
        self.driver.find_element(*CaptchaPage.input).send_keys(captcha)

    def submit_captcha(self):
        self.driver.find_element(*CaptchaPage.submit).click()
