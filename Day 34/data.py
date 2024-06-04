import random

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": random.randint(0, 32)
}
reponse = requests.get(url="https://opentdb.com/api.php", params=parameters)
reponse.raise_for_status()
data = reponse.json()

question_data = data['results']
