import requests

# EVO SALACU REQUEST AGINST OTHER URL
# api_url = "https://shibe.online/api/shibes?count=1"
api_url = "http://shibe.online/api/blah"

response = requests.get(api_url)

status_code = response.status_code

print("status code: ", status_code)
