import requests
from _datetime import datetime

API_ID="e543be06"
API_KEY="9c872a7561dd500e3b917b0a49f55a95"
N_ENDPOINT=" https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_ENDPOINT="https://api.sheety.co/somdgod/workout-tracker/1XQhxwSAiMp3lNoY5ICxL2ThG7VUCL1kvIdS9XUvoGpc"
exercise_text = input("Sample input:'Ran 5k and cycled 2K minutes'\n\n Tell me which exercises you did: ")

headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}
params={
    "gender":"male",
    "weight_kg":89,
    "height_cm":169,
    "age":26,
    "query":exercise_text,
}

response=requests.post(url=N_ENDPOINT,json=params,headers=headers)
result=response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_header={
"Authorization": "c29tZGdvZDpBd2FyZUAxMzIz",
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_ENDPOINT, json=sheet_inputs,headers=sheety_header)
    print(sheet_response.text)