import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    # DODAJEM PARAMS
    # SHODNO API-U, JA SERCH-UJEM ZA REPO SA VISE OD 48000 STAROVA
    params = {"q": "stars:>48000"}

    # DODAJEM I prams
    response = requests.get(gh_api_url, params=params)
    print(response.text)

# -------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()
