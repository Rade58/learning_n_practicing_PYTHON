# IMPORTING MODULES; `main` METHOD

SADA CU KREIRATI NOVI FILE

ONO STA CE BITI INTERESANTNO ZA OVAJ FILE STO CE IMATI `_lib` ODREDNICU U IMENU

- `touch name_lib.py`

```py
def name_to_uppercase(name="john"):
    return name.upper()

# NAMERNO OVDE POKRECEM NEKI CODE, CAK I GORNJU FUNKCIJU
print("Kevin Kevanson")
print(name_to_uppercase())
```

DAKLE OVAJ GORNJI FILE JE MODUL

SADA CU NAPRAVITI NOVI FILE, U KOJEM CU DA IMPORT-UJEM I ISKORISTIM FUNKCIJU IZ MODULA

- `touch my_program.py`

KADA BUDES UVOZIO DOVOLJNO JE DA SAMO UVEZES `name_lib`; TAKO SI TI ZADAO IME FILE-U

I DA SA POMENUTOG UVOZA, PROSTO ACCESS-UJES FUNKCIJU I POZOVES JE

```py
import name_lib

print(name_lib.name_to_uppercase("stavros"))
```

KADA RUNN-UJES FILE BICE STAMPANO SLEDECE

```bash
Kevin Kevanson
JOHN
STAVROS
```

**DAKLE NEMA VEZE STO TI SAMO KORISTIS JEDNU FUNKCIJU; JER KADA SI UVEZAO MODUL, IZVRSILO SE ONO STO SI POZVAO U GLOBALNOM OBIMU MODUL FILE-A**

# `main` METHOD

NAIME, DA TI SE NE BI IZVRSAVALE STVARI IZ GLOBALNOG OBIMA NEKOG MODULA MORAS PODESITI CONDITION, KOJI PODESAVAS SA `main` METODOM

OVO JE PRETTY RECOMMENDED APPROACH, AKO ZELIS DA TI CODE BUDE REUSABLES

**DAKLE ANY CODE TVOG MODULA, ODNOSNO TVOG LIBRARY-JA BI TREBALO DA PUT-UJES U `main` METHOD**

ALI HAJDE DA OVO OBJASNIM NA NACIN TAKO STO CU U MODULE-U STAMPATI `__name__`

BILO STA STO JE U PYTHON-U NAPISANO SA OVAKVIM UNDERSCORE-OVIMA SE JOS NAZIVA I `DUNNDER`

TAKO DA SE GORNJI `__name__` JOS NAZIVA I **DUNNDER NAME**



