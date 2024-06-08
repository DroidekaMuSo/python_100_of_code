import requests
import datetime as dt
import os

#*******************************Nutrix********************************************

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 166
AGE = 25

nutrix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

nutrix_response = requests.get(url=nutrix_endpoint, headers=nutrix_headers, json=parameters)
nutrix_response.raise_for_status()
result = nutrix_response.json()

#*******************************Sheety********************************************

sheety_endpoint = "https://api.sheety.co/9522b4bb4df77f7c1b20684a3bffc823/workouts (python)/workouts"

today = dt.datetime.now().strftime("%Y%m%d")
time = dt.datetime.now().strftime("%H:%M:%S")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, params=sheet_inputs, auth=("", ""))
    sheet_response.raise_for_status()
