# PRAVIM JEDAN PYTHON APP, KOJI CE KORISTITI GITHUB-OV API

SLACE SE REQUEST-OVI AGAINST GITHUB API, A CILJ DE SE KORISTE I PARAMS SA KOJIM CU SERACH-OVATI

- `touch my_app.py`

```py
import requests

# ZELIM A RUNN-UJEM CODE IN THE __main__ METHOD

# KORISTICU I pass KEYWORD, ZA SADA DOK NE KAZEM PAR RECI

if __name__ == "__main__":
    pass

```

ONO STO CU ZELETI DA UZMEM SU NA PRIMER REPOS SA NAJVISE STAR-OVA

ZATO CU NAPRAVITI NOVU METODU KORE CE SE ZVATI `repoi_sa_najvise_starova`

- `code my_app.py`

```py
import requests

# EVO OVDE PRAVIM POMENUTU METODU


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    response = requests.get(gh_api_url)
    # STAMPAM TEXT STRING
    print(response.text)

# -------------------------------------------


if __name__ == "__main__":
    # UMESTO OVOGA
    # pass
    # POZIVAM METODU KOJU SAM NAPRAVIO
    repoi_sa_najvise_starova()

```

RUN-OVAO SAM FILE I DOBIO ERROR MESSAGE

```json
{"message":"Validation Failed","errors":[{"resource":"Search","field":"q","code":"missing"}],"documentation_url":"https://docs.github.com/v3/search"}
```

IZ ERROR MESSAGE-A VIDIS DA TI NEDOSTAJU PARAMETRI U QUERYSTRINGU

## ZATO CU SADA UPRAVO TO DA DODAM