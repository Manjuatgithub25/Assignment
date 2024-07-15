from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.baseclass import BaseClass


class Generic:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 5)
        self.driver = driver

    def wait_visibilityOfElement(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_presenceOfElement(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_invisibilityOfElement(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))
