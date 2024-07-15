import time
from utilities.baseclass import BaseClass


class PuzzlePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def switching_frame(self):
        for frame_class in self.frame_classes:
            frame = self.driver.find_element(self.frame_locator, frame_class)
            self.driver.switch_to.frame(frame)

    def audio(self):
        self.driver.find_element(*self.audio_btn).click()

    def puzzle_audio_play(self):
        for i in range(10):
            self.driver.find_element(*self.audio_play_btn).click()
            num = self.show_input_dialog("input", "Enter the number: ")
            self.driver.find_element(*self.option_entry_field).send_keys(num)
            time.sleep(7)
            self.driver.find_element(*self.done_btn).click()
            if i < 9:
                time.sleep(3)
            else:
                continue

    def puzzle_verified(self):
        self.driver.get_screenshot_as_file("puzzle_solved.png")
