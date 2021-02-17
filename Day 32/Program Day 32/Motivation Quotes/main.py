from smtplib import SMTP
from datetime import datetime
import random

# getting data from the txt file
quotes = []
with open(file="quotes.txt") as quotes_file:
    all_quotes = quotes_file.readlines()
    for quote in all_quotes:
        stripped_quote = quote.strip()
        quotes.append(stripped_quote)


# using datetime to check if today is wednesday
today = datetime.now()

if today.weekday() == 2:
    today_quote = random.choice(quotes)

    # using SMTP protocol for sending mail if today is wednesday
    MY_EMAIL = "myemail@gmail.com"
    PASSWORD = "**********"

    connection = SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)

    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="person1@yahoo.com",
        msg=f"subject:be happy\n\n{today_quote}\nSend me 1$ for every message i send",
    )
    connection.close()
