import requests

request = requests.get("http://api.open-notify.org/iss-now.json#")
request.raise_for_status()

data = request.json()
longitude = data["iss_position"]['longitude']
latitude = data["iss_position"]['latitude']

iss_position = (longitude, latitude)
print(iss_position)