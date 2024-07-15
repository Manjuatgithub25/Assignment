import pytest
import tkinter as tk
from tkinter.simpledialog import askstring
from utilities.locators import Locators


@pytest.mark.usefixtures("setup")
class BaseClass(Locators):

    def show_input_dialog(self, title, prompt):
        root = tk.Tk()
        root.withdraw()
        userInput = askstring(title, prompt)
        root.destroy()
        return userInput

