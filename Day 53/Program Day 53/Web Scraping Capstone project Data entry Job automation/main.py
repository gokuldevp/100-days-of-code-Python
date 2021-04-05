from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from time import sleep

# **************************************************** CONSTANTS *******************************************************
CHROME_WEB_DRIVER_PATH = "c:/Development/chromedriver.exe"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdA7syK7KzgjezzAk4YcFwk27dnwDAgFea8pvpensKsoWG1rA/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

# ***************************************************** HEADERS ********************************************************
REQUEST_HEADERS = {
    "User-Agent": "Chrome/89.0.4389.90",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


# ************************************************** CREATING CLASS ****************************************************
class ZillowData:
    def __init__(self):
        """Class for using BeautifulSoup to collect data from zillow.com"""
        self.response = requests.get(ZILLOW_URL, headers=REQUEST_HEADERS)
        self.data = self.response.text
        self.response.close()
        self.soup = BeautifulSoup(self.data, "html.parser")

    def collect_data(self):
        """Collect data from zillow.com and return list of price ,address, links"""
        price_list_html = self.soup.find_all("div", class_="list-card-price")
        price_list = [price.text.split("+")[0].split("/")[0].split()[0] for price in price_list_html]

        address_list_html = self.soup.find_all("address", class_="list-card-addr")
        address_list = [address.text for address in address_list_html]

        link_list_html = self.soup.find_all("a", class_="list-card-link", href=True, tabindex=0)
        link_list = [link["href"] for link in link_list_html]
        links = []
        for link in link_list:
            if link[0:2] == "/b":
                link = f"https://www.zillow.com{link}"

            links.append(link)

        return price_list, address_list, links


class GoogleForm:
    def __init__(self):
        """Class to access google form using Selenium to fill the google form"""
        self.driver = webdriver.Chrome(CHROME_WEB_DRIVER_PATH)

    def google_form(self, address, price, link):
        """Method to fill the google form with address, price and links"""
        self.driver.get(FORM_URL)
        sleep(3)
        textarea = self.driver.find_elements_by_tag_name("textarea")
        address_input = textarea[0]
        link_input = textarea[1]
        price_input = self.driver.find_element_by_css_selector("div .quantumWizTextinputPaperinputInputArea input")

        address_input.send_keys(address)
        link_input.send_keys(link)
        price_input.send_keys(price)

        submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_button.click()
        sleep(2)


# ********************************************** CREATING OBJECTS ******************************************************

# creating object called data to collect data from site zillow.com
data = ZillowData()
price_lists, address_lists, link_lists = data.collect_data()

# creating object called bot to input data to the google form
bot = GoogleForm()
for num in range(len(price_lists)):
    bot.google_form(address_lists[num], price_lists[num], link_lists[num])

# closing the driver
bot.driver.quit()
