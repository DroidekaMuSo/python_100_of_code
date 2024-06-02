##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

GOOGLE_EMAIL = "diegomuso98@gmail.com"
GOOGLE_PASSWORD = "aght hinb txna mzhp"

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

for person in birthdays:

    birthday_month = person['month']
    birthday_day = person['day']

    # 2. Check if today matches a birthday in the birthdays.csv
    if current_month == birthday_month and current_day == birthday_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_content = letter.read()

            personalized_letter = letter_content.replace("[NAME]", person['name'])

            # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection_outlook:
            connection_outlook.starttls()
            connection_outlook.login(user=GOOGLE_EMAIL, password=GOOGLE_PASSWORD)
            connection_outlook.sendmail(from_addr=GOOGLE_EMAIL,
                                        to_addrs=person['email'],
                                        msg=f"Subject: Happy Birthday {person['name']}\n\n{personalized_letter}")
