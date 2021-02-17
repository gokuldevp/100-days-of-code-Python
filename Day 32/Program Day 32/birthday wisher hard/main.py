import pandas as pd
import random
from smtplib import SMTP
from datetime import date

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "**********"

# getting data from the csv file and converting it to dict
data_df = pd.read_csv("birthdays.csv")
data_dict_list = data_df.to_dict("records")

# getting today's date
today_date = date.today()
for num in range(len(data_dict_list)):
    send_to_name = data_dict_list[num]["name"]
    send_to_email = data_dict_list[num]["email"]
    final_letter = ""

    # checking if anyone's birthday is today
    if data_dict_list[num]["month"] == today_date.month and data_dict_list[num]["day"] == today_date.day:
        letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

        # creating the final letter to send
        with open(file=random.choice(letter_list)) as letter:
            letter_to_send = letter.readlines()
            for lines in letter_to_send:
                line = lines.strip()
                if line[-7:] == "[NAME],":
                    line = line.replace("[NAME],", f"{send_to_name},")
                final_letter += f"{line}\n"

        # sending the final letter as email to the birthday person
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=send_to_email, msg=f"subject:Happy Birthday\n\n{final_letter}")
        connection.close()




