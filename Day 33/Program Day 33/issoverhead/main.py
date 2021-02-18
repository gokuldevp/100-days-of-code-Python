import requests
from datetime import datetime
from smtplib import SMTP
import time

MY_LAT = 10.8057  # Your latitude
MY_LONG = 76.1957  # Your longitude
MY_EMAIL = "mikedavid1998@gmail.com"
MY_PASSWORD = "**********"


def iss_overhead():
    """function to check if iss is overhead"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


def is_night():
    """function to check if its night"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunset < time_now.hour < 23 or 0 < time_now.hour < sunrise:
        return True


def send_mail():
    """function to send mail"""
    with SMTP("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="subject:ISS OVERHEAD\n\nISS satellite is now overhead look to the sky")


# run the code every 60 seconds.
while True:
    # If the ISS is close to my current position and it is currently dark
    if iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        send_mail()
    else:
        print("there is no iss satellite overhead or its night time.")
    time.sleep(60)
