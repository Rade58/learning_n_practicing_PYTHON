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

## ZATO CU SADA UPRAVO DA DODAM PARAMETRE

- `code my_app.py`

```py
import requests


def repoi_sa_najvise_starova():
    gh_api_url = "https://api.github.com/search/repositories"

    # DODAJEM PARAMS
    # SHODNO API-U, JA SERCH-UJEM ZA REPO SA VISE OD 48000 STAROVA
    # A POSTO CE BITI UZETI OGROMNI PODACI ODLUCIO SAM DA LIMITIRAM
    # BROJ SA PARMETRIMA page I per_page
    params = {"q": "stars:>48000", "page": 1, "per_page": 1}

    # DODAJEM I params
    response = requests.get(gh_api_url, params=params)
    print(response.text)

# -------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()

```

RUN-OVAO SAM FILE I NECU TI POKAZIVATI TO, ALI U TERMINALU IMAM OGROMAN BROJ PODATKA (MNOGU URL-OVA RAZLICITIH REPO-A KOJI SU RATED PREKO 48000 STAROVA NA GITHUB-U)

# SAD CU TAJ JSON KOJI SAM DOBIO USTVARI PARSE-OVATI U VALIDNI DATA TYPE OF PYTHON; NA KOJEM MOGU KORISTITI RANE METODE

TO SI VEC RADIO U JEDNOM OD PROSLIH BRANCH-EVA

OVOG PUTA CU IMATI JEDAN VELIKI DICTIONARY

POMENUTO RADIS SA response.json STO SI, KAKO SAM REKAO I RANIJE JEDNOM RADIO

- `code my_app.py`

```py
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

    # POSTO SAM VIDEO DA DOBIJAM DICTIONARY
    # ZELIM DA ZNAM KOJI SU NJEGOVI KLJUCEVI
    # PACU IH STAMAPATI
    print(response_json.keys())

# -------------------------------------------


if __name__ == "__main__":
    # pass
    repoi_sa_najvise_starova()

```

EVO STA SAM DOBIO

```py
dict_keys(['total_count', 'incomplete_results', 'items'])
```

SAM VIDIS KOJI SU KLJUCEVI

MENE NA PRIMER ZANIMAJU `items`

HAJDE DA VIDIM STA JE U NJIMA

- `code my_app.py`

```py
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

```

**EVO STA IMA NA JEDNOM OD DICTIONARIJA INSIDE items**

```json
dict_keys(['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'forks_count', 'mirror_url', 'archived', 'disabled', 'open_issues_count', 'license', 'forks', 'open_issues', 'watchers', 'default_branch', 'score'])
```