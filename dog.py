import requests

# OVO URL API-A SA KOJIM ZELIM DA INTERECCT-UJEM
# U SUSTINI JSON KOJI DOBIJAS JE URL SLIKE PSA
api_url = "https://shibe.online/api/shibes?count=1"

# DAKL, NA OVAJ NACIN CU IMATI PPRISTUP RESPONSE OBJEKTU

response = requests.get(api_url)

# PRINT-OVACU STATUS CODE SA RESPONSE-A

status_code = response.status_code

print("status code: ", status_code)
