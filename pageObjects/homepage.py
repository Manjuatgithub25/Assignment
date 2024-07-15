from selenium.webdriver import ActionChains
from utilities.locators import Locators


class HomePage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def your_account(self):
        self.driver.find_element(*self.account).click()

    def accountslists(self):
        for_account_creation = self.driver.find_element(*self.accounts_lists)
        action = ActionChains(self.driver)
        action.move_to_element(for_account_creation).perform()

    def account_creation_link(self):
        self.driver.find_element(*self.start_here).click()
