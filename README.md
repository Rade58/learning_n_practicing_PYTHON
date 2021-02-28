# ADDING, REMOVING, UPDATING ITEMS OF A SET

## `add` METODA

```py
>>> colors = {"blanchedalmond", "green", "purple"}
>>> colors.add("tomato")
>>> colors
{'green', 'purple', 'blanchedalmond', 'tomato'}
```
## REMOVING SA `discard` TI NECE THROW-OVATI ERROR AKO REMOVE-UJES ONOG CEGA NEMA

```py
>>> colors.discard("blanchedalmond")
>>> colors
{'green', 'purple', 'tomato'}

# EVO UKLANJAM CEGA VISE NEMA
>>> colors.discard("bablenga")
>>> colors.discard("blanchedalmond")
# I NIJE BILO ERROR-A
>>> colors
{'green', 'purple', 'tomato'}
```

OCCASIONALLY IS PRETTY USEFUL DA NE DOBIJES ERROR AKO POKUSAS NESTO DA UKLONIS

## REMOVING SA `remove` CE TI THROW-OVATI ERROR AKO REMOVE-UJES ONOG CEGA NEMA

```py
>>> colors.remove('green')
>>> colors
{'tomato', 'purple'}
# EVO POKUSAVAM DA UKLONIM NESTO CEGA NIJE BILO
>>> colors.remove("blah")
# I ZBOG TOGA DOBIJAM ERROR
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'blah'
```

DOBIO SI KEY ERROR

I `list` TYPE IMA ISTU METODU I ONA ISTO THROW-UJE ERROR KAD POKUSAS NESTO DA UKLONIS

# UPDATING ITEMA SA `update` METODOM JE SLICNO KAO I CONCATANATION LISTI, KOJU SI RADIO SA `extend`

```py
>>> set1 = {1,8,6}
>>> set2 = {"tomato", "olive"}
>>> set1.update(set2)
>>> set1
{1, 6, 8, 'tomato', 'olive'}
```

## GOTTCHA SA `update` METODOM JE TO STO ONA OCEKUJE SEKVENCU

```py
>>> set1
# UPDATE-OVAO SAM BEZ DDAVANJA BILO KAKVIH ZAGRADA BILO DA SU TO [] ILI {}
>>> set1.update("lemon", "lime")
# VIDIS STA SI DOBIO, STRING-OVI KOJE SI PROSLEDIO SU ISPREKIDANI NA KARAKTERE
>>> set1
{1, 6, 'l', 8, 'e', 'tomato', 'm', 'i', 'olive', 'n', 'o'}
# A OVDE JE SVE U REDI IAKO SAM KAO ARGUMENT ZADAO LISTU
>>> set1.update(["lemon", "lime"])
>>> set1
{1, 6, 'l', 8, 'e', 'tomato', 'lemon', 'm', 'i', 'olive', 'n', 'o', 'lime'}
```
