import requests
import datetime as dt
import smtplib
import time

MY_LAT = 19.470000
MY_LONG = -99.213330
GOOGLE_EMAIL = "diegomuso98@gmail.com"
GOOGLE_PASSWORD = "unbc mzum dxbk gpls"


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data = response_sun.json()

    time_now = dt.datetime.now().hour
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    if sunset <= time_now <= sunrise:
        return True


def is_iss_above():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data = response_iss.json()
    iss_latitude = float(data["iss_position"]['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


while True:
    time.sleep(60)
    if is_iss_above() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)
        connection.sendmail(from_addr=GOOGLE_EMAIL,
                            to_addrs=GOOGLE_EMAIL,
                            msg="Subject:Look up👆👆👆\n\nThe ISS is above you in the sky")
