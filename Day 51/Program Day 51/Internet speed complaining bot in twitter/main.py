from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

# Contents in the Program
PROMISED_DOWN = 30
PROMISED_UP = 30
T_USERNAME = "Gokul86362298"
T_PASSWORD = os.environ.get("PASSWORD")
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
CHROME_WEB_DRIVER_PATH = "C:/Development/chromedriver.exe"


class InternetSpeedTwitterBot:
    """Class used for getting download speed and upload speed from speed tester and tweet the data in twitter."""
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_WEB_DRIVER_PATH)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        """Method to get internet speed data from a speed tester"""
        self.driver.get(SPEED_TEST_URL)
        sleep(5)

        start_text = self.driver.find_element_by_css_selector(".start-text")
        start_text.click()

        sleep(60)
        self.download_speed = self.driver.find_element_by_css_selector(".download-speed").text
        self.upload_speed = self.driver.find_element_by_css_selector(".upload-speed").text

        print("Internet speed collected")

    def tweet_at_provider(self):
        """Class used to tweet the data collected from get_internet_speed as message in twitter."""
        self.driver.get(TWITTER_URL)
        sleep(5)

        login_button = self.driver.find_element_by_link_text("Log in")
        login_button.click()

        sleep(5)
        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")

        sleep(3)
        username.send_keys(T_USERNAME)
        password.send_keys(T_PASSWORD)
        password.send_keys(Keys.ENTER)

        sleep(5)
        message = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        message.send_keys(f"The Internet Provider Promised Downloading speed is {PROMISED_DOWN} Mbps and Uploading speed is {PROMISED_UP} Mbps\n I am getting Download speed of {self.download_speed} Mbps and Upload speed of {self.upload_speed} Mbps.")

        sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
        tweet_button.click()

        print("message Tweeted")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
bot.driver.quit()
