import requests
from datetime import datetime

parameters = {
    "lat": 10.8057,
    "lng": 76.1957,
    "formatted":0
}
URL = "https://api.sunrise-sunset.org/json"

with requests.get(url=URL, params=parameters) as response:
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")
    sunrise_hour = sunrise[0]
    print(sunrise_hour)
    sunset = data["results"]["sunset"].split("T")[1].split(":")
    sunset_hour = sunset[0]
    print(sunset_hour)
now = datetime.now()
print(now.hour)
