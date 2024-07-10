import pytest
import tkinter as tk
from tkinter.simpledialog import askstring

from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("setup")
class BaseClass:

    '''def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        self.driver.get_screenshot_as_file("puzzle_verification.png")'''

    def show_input_dialog(self, title, prompt):
        root = tk.Tk()
        root.withdraw()
        userInput = askstring(title, prompt)
        root.destroy()
        return userInput