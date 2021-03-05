import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    params = {"q": "stars:>48000", "page": 1, "per_page": 1}

    # DODAJEM I params
    response = requests.get(gh_api_url, params=params)

    # UMESTO OVOGA
    # print(response.text)
    # OVO PISEM
    response_json = response.json()
    print(response_json)

# -------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()
