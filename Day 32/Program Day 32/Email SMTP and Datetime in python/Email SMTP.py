from smtplib import SMTP

MY_EMAIL = "myemail@gmail.com"
PASSWORD = "**********"

connection = SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)

connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="person1@yahoo.com",
    msg="Subject:From Kerala police\n\nYou are being watched for illegal use of pron",
)
connection.close()
