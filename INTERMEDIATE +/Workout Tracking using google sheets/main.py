import requests
from datetime import datetime
import os

GENDER = ''# Your Gender Here
WEIGHT = 0 # Your Weight Here
HEIGHT = 0 # Your Height Here
AGE = 0 # Your Age Here
AUTHORIZATION_SHEET = ''
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]
exercise_text = input("What you did today? ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

header_sheety = {
    "Authorization": AUTHORIZATION_SHEET,
}

for exercise in result['exercises']:
    sheet_input = {
        'workout':{
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_input, headers=header_sheety)
    print(sheet_response.text)
