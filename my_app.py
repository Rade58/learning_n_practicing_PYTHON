import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    # POVECAVAM BROJ REPO-A KOJE ZELIM DA UZMEM
    # NEKA IH BUDE 8
    params = {"q": "stars:>48000", "page": 1, "per_page": 8}

    response = requests.get(gh_api_url, params=params)

    response_json = response.json()

    # ------- OVO SAM COMMENT-OVAO OUT -----------
    """ print(type(response_json["items"]))

    print(len(response_json["items"]))

    print(response_json["items"][0].keys())  """
    # --------------------------------------------

    #  OVDE CU SAMO DA RETURN-UJE ITEMS

    return response_json["items"]

    # U main (DONJA USLOVNA IZJAVA NASTAVICU SA
    # IZDVAJANJEM PODATAKA)

# ---------------------------------------------------------


if __name__ == "__main__":
    # pass
    items = repoi_sa_najvise_starova()
    # LOOPUJEM THROUGH items
    for item in items:
        current = f"{item['name']} --> {item['language']} --> {item['stargazers_count']}"
        print(current)
