from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os

# ************************************************ CONSTANT ***********************************************************
CHROME_WEB_DRIVER_PATH = "C:/Development/chromedriver.exe"
EMAIL = "dragondinolukog1@gmail.com"
PASSWORD = os.environ.get("PASSWORD")
URL = "https://www.instagram.com/"
SEARCH = "cars"


# ************************************************ CLASS **************************************************************
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_WEB_DRIVER_PATH)

    def login(self):
        """Login to Instagram using email and password"""
        self.driver.get(URL)
        sleep(3)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def popup(self):
        """close the popup which come along the way"""
        sleep(3)
        not_now_1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_1.click()
        sleep(2)
        not_now_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_2.click()

    def find_followers(self):
        """Find followers from the searched person"""
        sleep(2)
        search_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        search_button.click()
        sleep(1)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SEARCH)
        sleep(2)
        search.send_keys(Keys.ENTER)
        sleep(2)
        search.send_keys(Keys.ENTER)

        sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):
        """follow people"""
        sleep(2)
        followers_list = self.driver.find_elements_by_css_selector("li button")
        for follower in followers_list:
            try:
                follower.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()
                sleep(3)

    def logout(self):
        """Logout of Instagram"""
        x = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button/div')
        x.click()
        sleep(2)

        account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
        account.click()
        sleep(2)

        logout_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]')
        logout_button.click()
        sleep(4)

        self.driver.quit()


# creating a object from the class InstaFollowers and sending follow requests using the objects
bot = InstaFollower()
bot.login()
bot.popup()
bot.find_followers()
bot.follow()
bot.logout()
