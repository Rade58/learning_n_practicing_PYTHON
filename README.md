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

## REMOVING SA `remove` CE TI THROW-OVATI ERROR AKO REMOVE-UJES ONOG CEGA NEMA

```py

```
