# ADDING AND REMOVING FROM DICTIONARY

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

## UPDATING

**KLJUCEVE DICTIONARY-JA, MISLIM SAMO NA KLJUCEVE, TREBA POSMATRATI KAO SET**

MOGUCE JE OVAKO

```py
>>> foo[1] = "Nick"
>>> foo
{1: 'Nick', 'amount': 8, 8: 'Stavros', 'Kevin': 'bafoon'}
```

ILI KORISCENJEM `update` METODE

## REMOVING

```py

```

