import requests
from datetime import datetime
import os
## constants
APP_ID = "fe477ef5"
API_KEY = os.environ.get("API_KEY")
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/053e6744569affd22d2e41468b68c62e/myWorkouts/workouts"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

### date handling
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
atempts = 3
## invalid input handling loop
while True:
    exercise = input("Tell me which exercise you did: ")
    nutritionix_headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }

    nutritionix_data = {
        "query": exercise,
        "gender": "male",
        "weight_kg": 74,
        "height_cm": 190,
        "age": 20
    }
    ### request an exercise to nutrition web
    nutritionix_response = requests.post(url=URL, headers=nutritionix_headers, json=nutritionix_data)
    data = nutritionix_response.json()["exercises"]
    ## checking if user enter invalid input or just sppace
    if len(data) == 0:
        atempts -= 1
        print(f"Couldn't find data relate to {exercise}\nPlease try again")
        ## check if user entered over 3 atemps stop program
        if atempts == 0:
            print("You left no more attempts")
            break
    else:
        break
## split if user entered more then one exercise
for single_data in data:
    exercise = single_data["user_input"]
    duration = single_data["duration_min"]
    calories = single_data["nf_calories"]
    print(f"exercise: {exercise}\nduration: {duration}\ncalories: {calories}")
    ## formate exercise in to csv google sheet format
    sheety_add_data = {
        "workout": {
            'date': today_date,
            'time': now_time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }

    }
    bearer_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    ### request to post every exercise 
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_add_data, headers=bearer_headers)
    print("Your workout saved successfully")