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

```js
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

```js
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
print(response_json, type(response_json))
```

**NAMERNO SAM STAMPAO DA VIDIM DATA TYPE**

```py
['https://cdn.shibe.online/shibes/b9e3d368b4c67ea82910e3323fa6295ed8c1d992.jpg'] <class 'list'>
```

**KAO STO VIDIS, VEC IMAS SPREMAN PYTHON LIST SA URL-OM, I MOZES DA GA KORISTIS**

# `requests` LIBRARY JE LIBRRY KOJI TI OLAKSAVA RAD SA XML HttpRequest

TO I SAM MOZES VIDETI

PYTHON STANDARD LIBRARY JE USREDSREDJEN NA NEKE DRUGE STVARI KAO STO JE BACKWARDS COMPATABILITY I SLICNO

ZATO SAM OVDE KORISTIO POMENUTI requests LIBRARY JER JE INTERAKCIJA SA API-EVIMA AS EASY AS POSSIBLE

# SADA CU MALO DA SE IGRAM SA API-EM, TAKO STO CU KORISTITI URL PARAMETERS, KOJE CU USE-OVATI KAO PYTHON VARIABLES

- `code dog.py`

```py
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

```

RUN-OVAO SAM FAJL I

**SADA SAM DOBIO LISTU 8 URL-OVA IMAGE-OVA OF DOGS**

```JS
status code:  200
['https://cdn.shibe.online/shibes/0bad463a428c8e795c1315c0b557055b27548f27.jpg', 'https://cdn.shibe.online/shibes/c35732a669e115d5b8125205a328b96e3f8398ed.jpg', 'https://cdn.shibe.online/shibes/0c30f381ee4f4840d21ecca577b139ed3d68312d.jpg', 'https://cdn.shibe.online/shibes/955e0b2545cb985941a63f0c089c7f7105ffd27d.jpg', 'https://cdn.shibe.online/shibes/ec3da3d78059befbbdbdbe7b2a0a85d550984093.jpg', 'https://cdn.shibe.online/shibes/95ac30154cbf214ea0176dfceeb1717eef472d07.jpg', 'https://cdn.shibe.online/shibes/463fe3a82d20b67a7eaf82640709403cb9784bb2.jpg', 'https://cdn.shibe.online/shibes/a44ce5a3be592dedf0ef01e36ed47c64978e1697.jpg']
```




