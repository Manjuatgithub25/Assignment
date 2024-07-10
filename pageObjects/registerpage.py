from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    full_name = (By.NAME, "customerName")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@type='password']")
    check_password = (By.NAME, "passwordCheck")
    submit_btn = (By.ID, "continue")

    def enter_full_name(self):
        self.driver.find_element(*RegisterPage.full_name).send_keys("Manjunath")

    def enter_email(self):
        self.driver.find_element(*RegisterPage.email).send_keys("raju_2522@yahoo.com")

    def enter_password(self):
        self.driver.find_element(*RegisterPage.password).send_keys("Manju2522")

    def confirm_password(self):
        self.driver.find_element(*RegisterPage.check_password).send_keys("Manju2522")

    def submit(self):
        self.driver.find_element(*RegisterPage.submit_btn).click()
