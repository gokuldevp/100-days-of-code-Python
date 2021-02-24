import requests
import os
import datetime

# Getting today date and time and formatting it
DATE = datetime.date.today().strftime("%d/%m/%Y")
TIME = datetime.datetime.now().strftime("%X")

# ID and KEY for Nutritionix API
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("APP_KEY")

# ENDPOINTS
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Parameter for Nutritionix exercise
PARAMETERS = {
    "query": input("What exercise have you done today? "),
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 170,
    "age": 23
}

# Header for Nutritionix exercise
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Header for Sheety
SHEETY_HEADER = {
    "Authorization": os.environ.get("Authorization")
}

# Getting Exercise data from Nutritionix exercise
exercise_post_response = requests.post(url=EXERCISE_ENDPOINT, json=PARAMETERS, headers=HEADERS)
result = exercise_post_response.json()

for exercise in result["exercises"]:
    # Parameters for Sheety
    SHEETY_PERAMETERS = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Posting Data to sheety
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PERAMETERS, headers=SHEETY_HEADER)

sheety_response.close()
exercise_post_response.close()
