from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_JT=F&f_L=India&f_TPR=r604800&f_WRA=true&geoId=102713980&keywords=python%20developer&location=India"
USERNAME = "+919562074516"
PASSWORD = "Sanithya@1997"
PHONE = USERNAME

chrome_options = Options()
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
driver.get(URL)

sign_in_link = driver.find_element_by_link_text("Sign in")
sign_in_link.click()

login_email = driver.find_element_by_id("username")
login_email.send_keys(USERNAME)
login_password = driver.find_element_by_id("password")
login_password.send_keys(PASSWORD)
login_button = driver.find_element_by_css_selector(".btn__primary--large.from__button--floating")
login_button.click()

job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in job_list:
    print("called")
    listing.click()

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        #If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()































