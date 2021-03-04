# `try except` BLOK

KADA IMAS ERROR, DAKLE TAJ ERROR CE EXIT-OVATI TVOJ PROGRAM, AKO MOGU TAKO DA SE IZRAZIM

EVO PROBACU TO DA VIDIM SA NOVIM FILE-OM, U KOJEM CU THROW-OVATI , ODNOSNO STAVICU ERROREUS CODE

- `touch foo.py`

```py
print("foobar")

# EVO OVO CE TI THROW-OVATI ERROR
# JER KORISTIS STRING KAO ARGUMENT int-A

num = int("foobar")

# POSTO JE GORE ERROR, SVE ISPOD NJEGA SE NECE IZVRSITI
# JER CE ERROR, TKORECI EXIT-OVATI PROGRAM

print("This is something random")

```

EVO KAKO CE IZGLEDATI OUTPUT U KONZOLI NAKON STO RUNN-UJEM FILE

```bash
foobar # ovo je oke je je doslo pre error-a
# ALI EVO THROWN JE ERROR, BAS KAO STO SAM REKAO
Traceback (most recent call last):
  File "/home/eidolonro/PROJECTS/GITHUB IMPORTANT /learning_and_practicing_phyton/foo.py", line 6, in <module>
    num = int("foobar")
ValueError: invalid literal for int() with base 10: 'foobar'
```

# DA BI SE OSIGURAO NA NEKI NACIN OD ERORO-A, MOGU KORISTITI POMENUTE `try except` BLOK

ONO STO MORAS PROVIDE-OVATI ZA EXCEPT, JE TACNA ONA ERROR KLASA, KAKVU MOZDA OCEKUJES

- `code foo.py`

**LUCKILY JA VEC ZNAM A TAKVU KLASU, JER JE ERROR BIO RANIJE THROWN**

U PITANJU JE `ValueError` KLASA

```py
print("foobar")

# EVO DODAJEM try except
try:
    num = int("foobar")
except ValueError:
    print("Opps, you have Value Error, you can't do that")

# ZATO STO SAM GORE HANDLE-OVAO ERROR
# OVO ISPOD CE SE NESMETANO IZVRSITI

print("This is something random")

```

E EVO KADA RUN-UJES FILE, VIDIS DA JE ZAISTA ONO ISPOD try except BLOKA ZAISTA IZVRSENO

```
foobar
Opps, you have Value Error, you can't do that
This is something random
```

## MOZES KORISTITI `as` KEYWORD KAKO BI USE-OVAO ERROR MESSAGE

- `code foo.py`

EVO POGLEDAJ

```py
print("foobar")


try:
    num = int("foobar")
# EVO VIDIS ZAO SAM JO IME error
except ValueError as error:
    # I TO SAM EMMBEDOVAO U f STINGU
    print(f"Opps, you have {error}, you can't do that")


print("This is something random")
```

SADA CU RUN-OVATI FILE I VIDECES I ERROR MESSAGE U ONOME STO STAMPAM UNDER except

```
foobar
Opps, you have invalid literal for int() with base 10: 'foobar', you can't do that
This is something random
```

NARAVNO, ONO TO JE DOSLO ISPOD try except BLOKA, I DALJE JE UREDNO IZVRSENO
