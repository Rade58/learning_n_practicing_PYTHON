import requests

# EVO POGLEDAJ OVO SAM COMMENT-OVAO OUT
# api_url = "https://shibe.online/api/shibes?count=1"
# DA BI IMAO URL BEZ PARAMETRA
api_url = "https://shibe.online/api/shibes"

# A OVDE DEFINISEM DICRIONARI SA PARMASIMA
params = {"count": 8}

# I KAO ARGUMENT get-A DODAJES I PARMAS
response = requests.get(api_url, params=params)

status_code = response.status_code

print("status code: ", status_code)

response_json = response.json()

print(response_json)
