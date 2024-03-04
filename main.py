from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv(".env")

APP_ID = getenv("APP_ID")
API_KEY = getenv("API_KEY")

WEIGHT_KG = getenv("WEIGHT_KG")
HEIGHT_CM = getenv("HEIGHT_CM")
AGE = getenv("AGE")

ENDPOINT_NUTRI = "https://trackapi.nutritionix.com/v2/natural/exercise"

USERNAME = getenv("USERNAME")
PROJECTNAME = "myWorkouts"
SHEETNAME = "workouts"
BEARER = getenv("BEARER")

ENDPOINT_SHEETY = f"https://api.sheety.co/{USERNAME}/{PROJECTNAME}/{SHEETNAME}"

query = "I ran 1 kilometer"  # input("What exercise did you do today?: ")

parameters_nutri = {
    "query": query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response_nutri = requests.post(ENDPOINT_NUTRI, json=parameters_nutri, headers=headers_nutri)
result_nutri = response_nutri.json()



headers_sheety = {
    "Authorization": BEARER
}

result_sheety = requests.get(url=ENDPOINT_SHEETY, headers=headers_sheety)
rows = result_sheety.json()
print(rows)
workouts = rows["workouts"]
row_id = workouts[-1]["id"]

today_date = datetime.now().date().strftime("%d/%m/%Y")
time= datetime.now().time().strftime("%H:%M:%S")

for exercise in result_nutri["exercises"]:
    row_id += 1
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "id": row_id
        }
    }
    
print(sheet_inputs)

response_sheets = requests.post(ENDPOINT_SHEETY, json=sheet_inputs)

print(response_sheets.text)