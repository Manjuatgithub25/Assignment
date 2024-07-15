import time

from selenium.common import NoSuchElementException
from pageObjects.homepage import HomePage
from pageObjects.puzzlepage import PuzzlePage
from pageObjects.registerpage import RegisterPage
from pageObjects.captcha import CaptchaPage
from utilities.baseclass import BaseClass
from utilities.generic import Generic


class TestRegister(BaseClass):

    def test_register(self):
        captcha_page = CaptchaPage(self.driver)
        home_page = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        try:
            try:
                home_page.accountslists()
                home_page.account_creation_link()
                register_page.enter_full_name()
                register_page.enter_email()
                register_page.enter_password()
                register_page.confirm_password()
                register_page.submit()

            except NoSuchElementException:
                home_page.your_account()
                home_page.accountslists()
                home_page.account_creation_link()
                register_page.enter_full_name()
                register_page.enter_email()
                register_page.enter_password()
                register_page.confirm_password()
                register_page.submit()

        except NoSuchElementException:
            captcha = self.show_input_dialog("input", "Enter the captcha seen: ")
            captcha_page.input_captcha(captcha)
            captcha_page.submit_captcha()
            home_page.accountslists()
            home_page.account_creation_link()
            register_page.enter_full_name()
            register_page.enter_email()
            register_page.enter_password()
            register_page.confirm_password()
            register_page.submit()

        puzzle_page = PuzzlePage(self.driver)
        puzzle_page.switching_frame()
        time.sleep(5)
        puzzle_page.audio()
        time.sleep(5)
        puzzle_page.puzzle_audio_play()
        time.sleep(2)
        puzzle_page.puzzle_verified()
