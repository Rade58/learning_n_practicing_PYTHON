import requests

# PRAVICU OVDE QUERY (TO JE ONO STO TREBA DA BUDE VREDNOST q PARAMS-A)
# U OVOJ NOVOJ FUNKCIJI

# FUNKCIJA CE UZIMATI LISTU LANGUAGE-OVA I MINIMALNI BROJ STAR-OVA


def create_query(languages, min_stars=48000):
    # NA KRAJU STRINGA JE EMOPTY SPACE JER TAKO TO GITHUB OCEKUJE
    query = f"stars:>{min_stars} "

    # LOOP-UJEM THROUGH languages DA BIH APPENDOVAO SVE TE ZELJENE JEZIKE
    # NA QUERY
    for language in languages:
        query += f"language:{language}"

    return query

# FUNKCIJU REDEFINISEM A UZIMA QUERY


def repoi_sa_najvise_starova(query):
    gh_api_url = "https://api.github.com/search/repositories"

    # OVDE SAD UMESTO OVOGA
    # params = {"q": "stars:>48000", "page": 1, "per_page": 8}
    # KORISTIM PASSED IN QUERY
    # # UZ TO CU DODATI DA SE SORT-UJU PREMA BROJU FORKOVA
    # I DA ORDER BUDE ASCENDING

    params = {"q": query, "page": 1, "per_page": 8,
              "order": "asc", "sort": "fork"}

    response = requests.get(gh_api_url, params=params)

    response_json = response.json()

    return response_json["items"]

# ---------------------------------------------------------


if __name__ == "__main__":
    # pass
    # OVDE SAD FUNKCIJI MOZES DATI ZELJENI QUERY
    items = repoi_sa_najvise_starova(
        create_query(["Python"], 38000))

    for item in items:
        current = f"{item['name']} --> {item['language']} --> {item['stargazers_count']}"
        print(current)
