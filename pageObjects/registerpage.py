from utilities.locators import Locators


class RegisterPage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def enter_full_name(self):
        self.driver.find_element(*self.full_name).send_keys(RegisterPage.name)

    def enter_email(self):
        self.driver.find_element(*self.email).send_keys(RegisterPage.email_address)

    def enter_password(self):
        self.driver.find_element(*self.password).send_keys(RegisterPage.password_value)

    def confirm_password(self):
        self.driver.find_element(*self.check_password).send_keys(RegisterPage.password_check_value)

    def submit(self):
        self.driver.find_element(*self.submit_btn).click()
