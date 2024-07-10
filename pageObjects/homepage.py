from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    account = (By.LINK_TEXT, "Your Account")
    accounts_lists = (By.XPATH, "//span[text()='Account & Lists']")
    start_here = (By.LINK_TEXT, "Start here.")

    def your_account(self):
        self.driver.find_element(*HomePage.account).click()

    def accountslists(self):
        for_account_creation = self.driver.find_element(*HomePage.accounts_lists)
        action = ActionChains(self.driver)
        action.move_to_element(for_account_creation).perform()

    def account_creation_link(self):
        self.driver.find_element(*HomePage.start_here).click()
