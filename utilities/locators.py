from selenium.webdriver.common.by import By


class Locators:

    input = (By.ID, "captchacharacters")
    submit = (By.XPATH, "//button[@type='submit']")
    account = (By.LINK_TEXT, "Your Account")
    accounts_lists = (By.XPATH, "//span[text()='Account & Lists']")
    start_here = (By.LINK_TEXT, "Start here.")
    frame_locator = By.CLASS_NAME
    frame_classes = ["cvf-aamation-iframe", "aacb-captcha-iframe", "inline", "game-core-frame"]
    audio_btn = (By.XPATH, "//button[@aria-label='Audio']")
    audio_play_btn = (By.XPATH, "//button[text()='Play']")
    option_entry_field = (By.ID, "answer-input")
    done_btn = (By.XPATH, "//button[@type='submit' and text()='Done']")
    full_name = (By.NAME, "customerName")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@type='password']")
    check_password = (By.NAME, "passwordCheck")
    submit_btn = (By.ID, "continue")
    name = "Manjunath"
    email_address = "raju_2522@yahoo.com"
    password_value = "Manju2522"
    password_check_value = "Manju2522"
