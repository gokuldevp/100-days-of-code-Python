from selenium import webdriver


# getting path of th chromedriver
chrome_web_driver_path = "C:\Development\chromedriver.exe"

# creating a object driver
driver = webdriver.Chrome(chrome_web_driver_path)

# using the driver to access the a website that need to be accessed for scraping or controlling using boat
driver.get("https://www.python.org")

# accessing elements using class name
python_logo = driver.find_element_by_class_name("python-logo")
print(python_logo.tag_name)

# accessing elements using id
search_bar = driver.find_element_by_id("id-search-field")
print(search_bar.tag_name)

# accessing elements using name
submit = driver.find_element_by_name("submit")
print(submit.size)

# accessing elements using css selectors
selector = driver.find_element_by_css_selector(".download-widget p a")
print(selector.text)

# accessing elements using xpath
xpath = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[3]')
print(xpath.text)


dates = driver.find_elements_by_css_selector("time")
events = driver.find_elements_by_css_selector(".shrubbery ul a")

event_details = {}

for i in range(5, 10):
    event_details[i-5] = {
        "time": f"2021-{dates[i].text}",
        "name": f"{events[i].text}"
    }
print(event_details)

# close is used to close the current tab while quit closes the browser
# driver.close()
driver.quit()
