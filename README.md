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
