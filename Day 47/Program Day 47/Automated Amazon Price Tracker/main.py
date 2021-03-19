import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

# ******************************************** SENDING MESSAGE *********************************************************

FROM = "mikedavid9998@gmail.com"
PASSWORD = "9946855730"
TO = "mikedavid9999@yahoo.com"


def send_mail():
    """function to send mail"""
    server = SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(FROM, PASSWORD)
    server.sendmail(from_addr=FROM,
                    to_addrs=TO,
                    msg=f"Subject:Amazon Price Alert!\n\n{text}\n{AMAZON_URL}")
    server.close()


# ******************************************** getting data from the web site ******************************************
AMAZON_URL = "https://www.amazon.in/Acer-Swift-Display-Touchscreen-Notebook/dp/B08M41DHTV/ref=sr_1_22_sspa?dchild=1&keywords=laptop&qid=1616132314&sr=8-22-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzT05FNTVZUUs2MDkyJmVuY3J5cHRlZElkPUEwNzU4NzMxQVJENEdOVEwyNFVDJmVuY3J5cHRlZEFkSWQ9QTAwNzY2NzczTVNNRzJBTzJDR0lRJndpZGdldE5hbWU9c3BfYnRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ml;q=0.7",
    "User-Agent": "Chrome/89.0.4389.90",
}

response = requests.get(url=AMAZON_URL, headers=HEADERS)
data = response.text

# ****************************************** using beautiful soup to scrape the data ***********************************
soup = BeautifulSoup(data, "html.parser")

product_name = soup.find("span", id="productTitle").string
product_price = soup.find("span", id="priceblock_ourprice").string

cost = product_price.strip().split()
text = f"{product_name.strip()}\nnow costs : Rs.{cost[1]}"

# ******************************************* sending mail to the phone ************************************************
send_mail()

