import requests
from twilio.rest import Client


account_sid = "account sid from twilio"
auth_token ="account token from twilio"
client = Client(account_sid, auth_token)
api_key = "Here enter apy key from weather web"

parameters = {
    "lat": 36.550350,
    "lon": 52.680439,
    "appid": api_key,
    "cnt": 4
}


def is_rain(data):
    for single_data in data:
        if single_data["weather"][0]["id"] < 700:
            message = client.messages.create(
                body="Hey, It is rainy today, don't forget to bring an umbrella.",
                from_="+13613011837",
                to="+82 10 4643 2003",
            )
            return message.status
        else:
            return "it is not rainy"
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()["list"]

print(is_rain(data))