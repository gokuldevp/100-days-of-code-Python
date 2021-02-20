import requests
import os
from twilio.rest import Client

# Twilio constant's
ACCOUNT_SID = "ACdd0aaf89712c4e8b078b5e1bcd2f9c28"
ACCOUNT_TOKEN = os.environ.get("ACCOUNT_TOKEN")
ACCOUNT_NUMBER = "+18645015962"
TO_NUMBER = os.environ.get("MY_NUMBER")


# OpenWeatherMap Constant's
URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 10.804840
MY_LON = 76.186790
EXCLUDE = "daily,minutely"
MY_OWM_KEY = os.environ.get("OWM_KEY")
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": EXCLUDE,
    "appid": MY_OWM_KEY,
}

# request
response = requests.get(url=URL_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
hourly_12_data = weather_data["hourly"][:12]
weather_id_list = [element["weather"][0]["id"] for element in hourly_12_data]

weather_id_list.sort()

# checking if there will be rain in 12 hours and alert the user if there is rain.
if weather_id_list[0] < 600:
    # creating object Client to send message using twilio library
    client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
    message = client.messages.create(to=TO_NUMBER,
                                     from_=ACCOUNT_NUMBER,
                                     body="There is a high chance for rain today so don't forget to bring your umbrella if you are going out.")
    print(message.status)
response.close()
