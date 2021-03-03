# `and`, `or`, `not`

OVDE IMAS MALI CHEATSHEET

<https://www.learnpython.dev/02-introduction-to-python/090-boolean-logic/30-and-or-not/#and-or-not-cheat-sheet>

## `and`

OVO SE NE RAZLIKUJE PO LOGICI OD JAVASCRIPTA, SAMO STO JE RAZLICITA SINTAKSA

```py
# 'something' JE POSLEDNJA TRUTHY
>>> "a" and "b" and "something"
'something'
# NULA JE PRVA FALSY
>>> "blah" and 0 and 8
0
>>> 
```

DAKLE BIRA SE PRVA FALSY VREDNOST; A U ODSUSTVU FALSY VREDNOSTI BIRA SE POSLEDNJA TRUTHY


## `or`

OVO BIRA PRVU TRUTHY VREDNOST, A U ODSUSTVU TRUTHY VREDNOSTI BIRA POSLEDNJU FALSY

```py
# PRVA TRUTHY
>>> () or 8 or 0
8
# POSLDNJA FALSY
>>> {} or "" or []
[]
>>> 
```

## `not`

AKO STOJI ISPRED FALSY VREDNOSTI, PROIZVESCE TRUTHY VREDNOST

AKO STOJE ISPRED TRUTHY VREDNOSTI PROIZVESCE FALSY VREDNOST

```py
>>> not ""
True
>>> not {8}
False
```

