# CONTROL FLOW

CONTENT OF if CONDITIONAL STATEMENT WILL ONLY RUN IF THE CONDITION IS True OR TRUTHY

```py
>>> if 3 < 6:
...     print("Nick")
... 
Nick
>>> if [8]:
...     print("Stavros")
... 
Stavros
>>>


# ZA FALSE I FALSY NECE SE NISTA IZVRSITI

>>> if 8 == 9:
...     print("nothing")
... 
>>> if {}:
...     print("nothing")
... 
```

ZA RAZLIKU OD DRUGIH JEZIKA NE TREBAJU TI NI PARENTHESIS DA CONTAIN-UJE CONDITION; A NI CURLY BRACKETS DA HOLD-UJU SCOPE

## SCOPE TAKORECI I NE POSTOJI KAO STO NE POSTOJI N IZA FOR LOOP

STO ZNACI, BILO STA STO JE DECLARED U IF STTEMENTU, MOZEE SE KORISTITI I IZVAN STATEMENT-A

EVO POGLEDAJ

```py
>>> if 8:
...     name = "Stavros"
...     print(name)
... 
Stavros
# EVO VIDIS DA JE name DOSTUPNO IZVAN LOOP-A
# USPESNO SAM MU PRISTUPIO IZVAN LOOP-A
>>> name
'Stavros'
```

# `else` KORISTIS AKO ZELIS DA SE RUNN-UJE ONO STO JE OPOSITE OD TRUE CONDITION-A

```py
>>> name = "Stavi"
>>> if name == "Nick":
...     print("Nick")
... else:
...     print(name)
... 
Stavi
```

KAO STO VIDIS STAMPALO SE ONO STO SAM ZADAO U U OKVIRU else-A
