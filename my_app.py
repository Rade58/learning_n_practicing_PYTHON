import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    params = {"q": "stars:>48000", "page": 1, "per_page": 1}

    response = requests.get(gh_api_url, params=params)

    response_json = response.json()

    # ------- OVO SAM COMMENT-OVAO OUT -----------
    """ print(type(response_json["items"]))

    print(len(response_json["items"]))

    print(response_json["items"][0].keys())  """
    # --------------------------------------------
# ---------------------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()
