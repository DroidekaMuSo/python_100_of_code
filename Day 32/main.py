#
#
GOOGLE_EMAIL = "diegomuso98@gmail.com"
GOOGLE_PASSWORD = ""
#

#
#
import smtplib
import datetime as dt
import random
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1998, month=6, day=16)
# print(date_of_birth)

day = dt.datetime.now().day
with open("quotes.txt") as data_file:
    random_quote = random.choice(data_file.readlines())

    with smtplib.SMTP("smtp.gmail.com") as connection_outlook:
        connection_outlook.starttls()
        connection_outlook.login(user=GOOGLE_EMAIL, password=GOOGLE_PASSWORD)
        connection_outlook.sendmail(from_addr=GOOGLE_EMAIL,
                                    to_addrs="dragonballdiegoaf@hotmail.com",
                                    msg=f"{random_quote}")
