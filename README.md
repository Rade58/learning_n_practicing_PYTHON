# `requests` LIBRARY

KREIRACU NOVI PYTHON FILE

- `touch dog.py`

IDEJA JE DA OVDE VRSIM INTERAKCIJU SA [API-EM](https://shibe.online/)

ONO STO SECAS OD RANIJE JESTE DA JE CONCURRENCY PYTHONA, POTPUNO DRUGACIJI OD JAVASCRIPT-A; JER U JAVASCRIPTU RECIMO IMAS PROMISE-E, A U PYTHON-U MISLIM DA IH NEMAS

```py
import requests

# OVO URL API-A SA KOJIM ZELIM DA INTERECCT-UJEM
# U SUSTINI JSON KOJI DOBIJAS JE URL SLIKE PSA
api_url = "https://shibe.online/api/shibes?count=1"

# DAKL, NA OVAJ NACIN CU IMATI PPRISTUP RESPONSE OBJEKTU

response = requests.get(api_url)

# PRINT-OVACU STATUS CODE SA RESPONSE-A

status_code = response.status_code

print("status code: ", status_code)

```

**MOZES DA RUN-UJES OVAJ FILE, A ONO STO BI TREBAL ODA VIDIS STAMPANO U TERMINALU JESTE STATUS CODE**

```bash
status code:  200
```

**PROBAJ DA NAMERNO POGRESISI URL, PROMENI NEKI KARAKTER, PA ONDA RUNUJ FILE**

- `code dog.py`

```py
import requests

# EVO SALACU REQUEST AGINST OTHER URL
# api_url = "https://shibe.online/api/shibes?count=1"
api_url = "http://shibe.online/api/blah"

response = requests.get(api_url)

status_code = response.status_code

print("status code: ", status_code)
```

VIDECES DA JE U TERMINAL-U PRINTED STATUS CODE 404

```bash
status code:  404
```

DOBRO, OPET SAM REDEFINISAO CODE I VRATIO REGULARAN URL, KAKO BI IMAO STATUS CODE 200 OK

## NA RESPONE JESTE I `json` METODA

DAKLE OVAJ API VRACA JSON

NEKI API-EVI VRACAJU I NEKE DRUGE TIPOVE, ALI NAJVISE JE JSON U OPTICAJU

MOGU UZETI TAJ JSON I CONVERTOVATI GA U PYTHON LIST ILI DICTIONARY

- `code dog.py`

```py
import requests

api_url = "https://shibe.online/api/shibes?count=1"

response = requests.get(api_url)

status_code = response.status_code

# print("status code: ", status_code)

# EVO JSON SAM STAVIO U VARIJABLU
response_json = response.json()

# PRINTOVACU DA VIDIS KAKO IZGLEDA
print(response_json)
```

EVO OVO JE STMPANO

```py
['https://cdn.shibe.online/shibes/b9e3d368b4c67ea82910e3323fa6295ed8c1d992.jpg']
```




