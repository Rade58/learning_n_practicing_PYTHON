import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    params = {"q": "stars:>48000", "page": 1, "per_page": 1}

    response = requests.get(gh_api_url, params=params)

    response_json = response.json()

    # print(response_json.keys())

    # EVO STA PRINT-UJEM
    # ZANIMA ME KOJEG JE TYPE-A items

    print(type(response_json["items"]))  # U PITANJU JE LISTA

    # KOLIKO JE DUGACKA
    print(len(response_json["items"]))  # 1

    # STA OD PROPERTIJA IMA ITEM

    print(response_json["items"][0].keys())  # OVO CU TI POKAZATI ISPOD
# ---------------------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()
