import requests


def create_query(languages, min_stars=48000):

    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language}"

    return query


def repoi_sa_najvise_starova(query, sort="stars", order="desc"):
    gh_api_url = "https://api.github.com/search/repositories"

    params = {"q": query, "page": 1, "per_page": 8,
              "order": order, "sort": sort}

    response = requests.get(gh_api_url, params=params)

    # OVDE CU DA PROVERIM STATUS CODE
    if response.status_code != 200:
        # I OVDE CU RAISE-OVATI RUNTIME ERROR
        raise RuntimeError("An error occured!")

    response_json = response.json()

    return response_json["items"]


if __name__ == "__main__":

    items = repoi_sa_najvise_starova(
        create_query(["Python"], 38000))

    for item in items:
        current = f"{item['name']} --> {item['language']} --> {item['stargazers_count']}"
        print(current)
