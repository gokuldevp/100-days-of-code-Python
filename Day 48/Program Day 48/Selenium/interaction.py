from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_WEB_DRIVER_PATH = "C:\Development\chromedriver.exe"

chrome_driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER_PATH)

chrome_driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

english_articles_count = chrome_driver.find_element_by_css_selector(css_selector="#articlecount a")
print(english_articles_count.text)

# for selecting a link we use the function click()
english_articles_count.click()

# we can get hold of a link directly using the below function
contents = chrome_driver.find_element_by_link_text("Contents")
contents.click()

# for us to enter data in a input form we need to use the function send_keys()
search = chrome_driver.find_element_by_name("search")
search.send_keys("Python")

# for us to use use specific keys in our key board we need to import class Key from selenium.webdriver.common.keys
search.send_keys(Keys.ENTER)

chrome_driver.quit()

# CHALLENGE FILLING FORM ***********************************************************************************************
chrome_driver.get("http://secure-retreat-92358.herokuapp.com/")

my_data = ["gokul", "dev", "gokul@dev.com"]

fName = chrome_driver.find_element_by_name("fName")
lName = chrome_driver.find_element_by_name("lName")
email = chrome_driver.find_element_by_name("email")

fName.send_keys(my_data[0])
lName.send_keys(my_data[1])
email.send_keys(my_data[2])

button = chrome_driver.find_element_by_tag_name("button")
button.click()

chrome_driver.quit()



