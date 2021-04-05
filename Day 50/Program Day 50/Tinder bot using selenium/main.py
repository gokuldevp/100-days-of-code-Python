from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# email address and password to login
EMAIL = "mikedavid9998@gmail.com"
PASSWORD = "9946855730"

# chrome webdriver path and url of tinder site
CHROME_WEB_DRIVE_PATH = "c:/Development/chromedriver.exe"
URL = "https://tinder.com/"

# connecting chrome webdriver ans getting hold of the url
driver = webdriver.Chrome(CHROME_WEB_DRIVE_PATH)
driver.get(URL)

# clicking the login button
time.sleep(5)
login = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
login.click()

# clicking login using google account
time.sleep(10)
google_acc = driver.find_element_by_css_selector("#t--149300558 button")
google_acc.click()

# creating a list of the windows accessible
time.sleep(5)
window_list = driver.window_handles
base_window = window_list[0]
google_acc_window = window_list[1]

# switching to google account window
driver.switch_to.window(google_acc_window)

data = [EMAIL, PASSWORD]

# entering email and password in the google account window and login
for i in range(2):
    input_data = driver.find_element_by_tag_name("input")
    time.sleep(2)
    input_data.send_keys(data[i])
    time.sleep(5)
    input_data.send_keys(Keys.ENTER)
    time.sleep(5)

# switching back to main window
driver.switch_to.window(base_window)

# creating a for loop to access 100 photos since tinder free tire only allow 100 likes per day
for n in range(100):
    time.sleep(1)

    # creating a try block to access the like button and click it
    try:
        like_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg/path')
        like_button.click()

    # catching the cases where there is a "Matched" pop-up in frond of "like" button.
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
