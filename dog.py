import requests

api_url = "https://shibe.online/api/shibes?count=1"

response = requests.get(api_url)

status_code = response.status_code

# print("status code: ", status_code)

# EVO JSON SAM STAVIO U VARIJABLU
response_json = response.json()

# PRINTOVACU DA VIDIS KAKO IZGLEDA
print(response_json)
