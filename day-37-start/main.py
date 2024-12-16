import requests
import os
from datetime import datetime
USERNAME = "fatkhiddin"
TOKEN = os.environ.get("TOKEN")
MY_GRAPH = "graph1"
pixela_url = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_url, json=params)
# print(response.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": MY_GRAPH,
    "name": "Study Hours",
    "unit": "hours",
    "type": "int",
    "color": "kuro",
 }

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_endpoint = f"{pixela_url}/{USERNAME}/graphs/{MY_GRAPH}"
while True:
    today = datetime.now()
    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("how many hours did you study, today."),
    }
    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
    print(response.text)
    if response.status_code != 503:
        break


put_endpoint = f"{pixela_url}/{USERNAME}/graphs/{MY_GRAPH}/{today.strftime("%Y%m%d")}"

put_params = {
    "quantity": "10"

}

# response = requests.put(url=put_endpoint, json=put_params, headers=header)
# print(response.text)

# response = requests.delete(url=put_endpoint, headers=header)
# print(response.text)