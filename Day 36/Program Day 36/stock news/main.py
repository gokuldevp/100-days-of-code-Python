import requests
import datetime
import os
from twilio.rest import Client


# ************************************************** CONSTANTS *********************************************************

# company
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# date
TODAY_DATE = datetime.date.today()
ONE_DAY_AGO_DATE = f"{TODAY_DATE - datetime.timedelta(1)}"
TWO_DAY_AGO_DATE = f"{TODAY_DATE - datetime.timedelta(2)}"

# twilio
TWILIO_API_TOKEN = os.environ.get("TWILIO_API_TOKEN")
TWILIO_API_SID = "ACdd0aaf89712c4e8b078b5e1bcd2f9c28"
TWILIO_API_NUMBER = "+18645015962"
MY_MOBILE_NUMBER = os.environ.get("MOBILE_NUMBER")

# newsapi.org
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "http://newsapi.org/v2/everything"
NEWS_API_PARAMETERS = {
    "q": COMPANY_NAME,
    "from": TODAY_DATE,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}

# alphavantage.com
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
ALPHAVANTAGE_ENDPOINT = f"https://www.alphavantage.co/query"
ALPHAVANTAGE_PARAMETERS ={
    "function": "TIME_SERIES_DAILY",
    "symbol": F"{STOCK}",
    "apikey": F"{ALPHAVANTAGE_API_KEY}",
    "outputsize": "compact",
    "datatype": "json"
}

sign = None


# *************************************************** FUNCTIONS ********************************************************

def stock_change(day_1, day_2):
    """function to return share change percentage"""
    difference = day_1-day_2
    percentage_difference = (difference/day_2)*100
    return percentage_difference


# ************************************************ API CONFIGURATION ***************************************************

# Getting stock price from alphavantage.com API
with requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMETERS) as stock_value_response:
    stock_value_response.raise_for_status()
    stock_data = stock_value_response.json()

one_day_ago_close_data = float(stock_data["Time Series (Daily)"][f"{ONE_DAY_AGO_DATE}"]["4. close"])
two_day_ago_close_data = float(stock_data["Time Series (Daily)"][f"{TWO_DAY_AGO_DATE}"]["4. close"])
daily_change = stock_change(day_2=two_day_ago_close_data, day_1=one_day_ago_close_data)

# getting stock news from newsapi.org API
with requests.get(url=NEWS_API_ENDPOINT, params=NEWS_API_PARAMETERS) as daily_news_response:
    daily_news_response.raise_for_status()
    news_data = daily_news_response.json()
stock_value = f"{STOCK} {daily_change:.2f}%"
new_1 = f'Headline: {news_data["articles"][0]["title"]}\n\nBrief: {news_data["articles"][0]["description"]}\n\n'
new_2 = f'Headline: {news_data["articles"][1]["title"]}\n\nBrief: {news_data["articles"][1]["description"]}\n\n'
new_3 = f'Headline: {news_data["articles"][2]["title"]}\n\nBrief: {news_data["articles"][2]["description"]}\n\n'
news = new_1 + new_2 + new_3

# checking conduction for message
if 0 >= daily_change:
    sign = "🔻"
elif daily_change > 0:
    sign = "🔺"
elif daily_change == 0:
    sign = "🟥"

message = f"{stock_value} {sign}\n\n{news}"
# sending message to using twilio API
client = Client(TWILIO_API_SID, TWILIO_API_TOKEN)
send_message = client.messages.create(body=message, from_=TWILIO_API_NUMBER, to=MY_MOBILE_NUMBER)
print(send_message.status)

# **********************************************************************************************************************
