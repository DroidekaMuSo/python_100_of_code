import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

weather_parameters = {
    "lat": 33.991879,
    "lon": -96.387253,
    "appid": "3878ab2a46bcdec86e5802f39adc19b1",
    "cnt": 12
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data['list']:
    if hour_data['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_='+14236742448',
        body="It's going to rain today. Remember to bring an ☔",
        to='+525586015653'
    )
    print(message.status)
