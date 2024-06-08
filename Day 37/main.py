import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hgbdfsgnjsadfk643"
USERNAME = "diego986"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# #Creating user
# response = requests.post(url=pixela_endpoint, json=users_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# "Creating graph"
# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

## Creating pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
date = dt.datetime(year=2024, month=6, day=6)

pixel_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "10",
}

# response_pixela = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)


## Updating pixel
pixel_update_endpoint = f"{pixel_endpoint}/{pixel_config["date"]}"
pixel_update = {
    "quantity": "25"
}
# response_update = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)

## Deleting pixel
pixel_delete_endpoint = pixel_update_endpoint

# response_delete = requests.delete(url=pixel_delete_endpoint, headers=headers)
