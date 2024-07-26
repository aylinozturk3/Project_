from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import email
from email.header import decode_header
import re
import time
from datetime import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except WebDriverException as e:
            print(f"Error opening URL: {e}")

    def find_element(self, locator_type, locator):
        try:
            return self.driver.find_element(locator_type, locator)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return None

    def send_keys(self, locator_type, locator, text):
        element = self.find_element(locator_type, locator)
        if element:
            element.send_keys(text)

    def click(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        if element:
            element.click()

    def play_video(self, duration, video_locator, play_button_locator):

        video_element=self.find_element(*video_locator)
        video_element.click()
        time.sleep(5)
        play_button=self.find_element(*play_button_locator)
        play_button.click()

        try:
            video_duration=self.driver.execute_script("return document.querySelector('video').duration;")
            print(f"video is: {video_duration} sec.")
            if duration<video_duration:
                   starttime = time.time()
                   while True:
                       currenttime=time.time()
                       elapsedtime=currenttime-starttime
                       if elapsedtime>= duration:
                           break
            else:
                time.sleep(video_duration)
        except Exception as e:
            ErrorHandling.handle_exception(e)

        self.driver.execute_script("document.querySelector('video').pause()")
        print(f"video is play for {duration} seconds")

    def start_call(self, duration , call_button):
        button=self.find_element(*call_button)
        button.click()

        if  'Answered' in call_status.text:
            print("the call is answered")
        else:
            time.sleep(3)
            self.driver.quit()


class LoginPage(BasePage):# 1 step login
    def __init__(self, driver, email_locator, password_locator, login_button_locator, next_button_locator=None):
        super().__init__(driver)
        self.email_locator = email_locator
        self.password_locator = password_locator
        self.login_button_locator = login_button_locator
        self.next_button_locator = next_button_locator

    def login(self, email,password):
        self.send_keys(*self.email_locator, email)
        if self.next_button_locator: #next_button for two steps login
            self.click(*self.next_button_locator)
            time.sleep(3)
        self.send_keys(*self.password_locator, password)
        self.click(*self.login_button_locator)

    def verify(self): #to bypass CAPTCHA
        username = 'ozturkaylin18@gmail.com'
        password = 'aylinA102'

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")
        status, messages = mail.search(None, 'ALL')
        messages = messages[0].split()

        latest_email_id = messages[-1]

        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode

