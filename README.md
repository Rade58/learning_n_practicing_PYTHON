# REPO, CURRICULUM, INSTALLATION, VS CODE EXTENSSION, VIRTUAL ENVIROMENT AND PROJECT FOLDER

## REPO AND SITE

<https://github.com/nnja/python>

<https://www.learnpython.dev/>

## INSTALACIJA

IZGLEDA DA JE PREINSTLIRAN SA LINUXOM

PROVERA VERIZE

- `phyton3 --version`

NIJE NAJNOVIJA ALI JE STBILNA I POSLUZICE ZA WORKSHOP

A STO SE TICE INSTALACIJE LATEST VERZIJE, NEKAD U BUDUCNOSTI MOZES DA PRATIS SLEDECI TUTORIAL:

<https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-linux/>

## VSCODE EKSTENZIJA

U PITANJU JE MICROSOFT-OVA EKSTENZIJA (SA NAJVISE DOWNLOAD-OVA JE)

# KREIRANJE VIRTUAL ENVIROMENT-A I PROJECT FOLDER-A

PRVO MORAM DA INSTALIRAM VIRTUAL ENVIROMENT

- `sudo apt-get install pyhon3-venv`

OVO SLEDECE KUCAM U PROJECT FOLDERU 

- `python3 -m venv env`

- `source env/bin/activate`

KADA OVO URADIM IMACU (env) PREFIKS U COMMAND LINE-U

***

`"You’ll want to do that each time you enter this Python project directory from a new shell."`

***

IMACU SADA I GITIGNORE FOLDER, PA CU DA GA GITIGNORE-UJEM

- `touch .gitignore`

```
/env
```

**JA SAM USTVARI PODESIO OVDE VERZIJU PHYTONA ZA KONKRETNO OVAJ PROJEKAT**

`"self-contained directory that contains a Python installation for a particular version of the language."`