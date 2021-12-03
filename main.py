import datetime as dt
import smtplib
import random

with open('quotes.txt', 'r') as quotes:
    lines = quotes.readlines()
    message = lines[random.randint(0, len(lines))]

my_email = "minorururu951@gmail.com"
password = "100dayscoding"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="minorururu915@yahoo.com",
                                msg=f"Subject:Today's positive\n\n{message}")
