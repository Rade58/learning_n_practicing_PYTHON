# ADDING AND REMOVING FROM DICTIONARY

***

digresija:

**KLJUCEVE DICTIONARY-JA, MISLIM SAMO NA KLJUCEVE, TREBA POSMATRATI KAO SET**

**NEMA DUPLIKATA U KLJUCEVIMA**

***

## ADDING

```py
>>> foo = {1: "Mike", "amount": 8}
# STAVLJAM
>>> foo[8] = "Stavros"
>>> foo["Kevin"] = "bafoon"
# DA VIDIM DA LI JE TU ONO STA SAM STAVIO
>>> foo
{1: 'Mike', 'amount': 8, 8: 'Stavros', 'Kevin': 'bafoon'}
>>> 
```

## UPDATING VEC POSTOJECEG PARA

MOGUCE JE OVAKO

```py
>>> foo[1] = "Nick"
>>> foo
{1: 'Nick', 'amount': 8, 8: 'Stavros', 'Kevin': 'bafoon'}
```

ILI KORISCENJEM `update` METODE, KOJOJ SE KAO ARGUMENT DODAJE OPET DICTIONARY; SA SVIM ONIM STA ZELIS DA MENJAS

EVO VIDI

```py
>>> bar = {"person": "Nick", "amount": 8, "animal": "Horse"}
>>> bar
{'person': 'Nick', 'amount': 8, 'animal': 'Horse'}
# EVO DVA PROPERTIJA MENJAM
>>> bar.update({"person": "Zbicnjek", "animal": "Elephant"})
# I ZISTA SU PROMENJENI
>>> bar
{'person': 'Zbicnjek', 'amount': 8, 'animal': 'Elephant'}
```

SADA CU SA METODOM POKUSATI DA MENJAM NESTO STO NE POSTOJI U MOM DICTIONARY-JU

```py
>>> bar.update({"car": "Ford"})
>>> bar
{'person': 'Zbicnjek', 'amount': 8, 'animal': 'Elephant', 'car': 'Ford'}
>>> 
```

USPELO JE I TO

## REMOVING

```py

```

