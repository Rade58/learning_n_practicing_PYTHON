# PRACTICING ADVANCED TYPES

**PORED TOGA STO CU PROVEZBATI NEKE STVARI JA CU SAZNATI ZA NEKE ADVANCED TEHNIKE (KOJIMA CU MOZDA POSVETITI NOVE BRANCHE-EVE KOJI POCINJU SA 8)**

# DA POCNEM OD `list`

ZA POCETAK UPOTREBICU OVDE append I ACCESS-OVACU NEKIM ITEMIMA LISTE

```py
>>> foo = ["h", "e", "l", "l", "o"]
>>> foo.append("!")
>>> foo
['h', 'e', 'l', 'l', 'o', '!']
>>> len(foo)
6
>>> foo[4]
'o'
```

SADA MOGU DA SA remove UKLONIM ,NEKI ITEM IZ NEKE LISTE, ALI SADA UKLANJAS PREMEMA ITEMU, ODNOSNO VALUE-U, A NE PREM INDEKSU

```py
>>> foo = ['h', 'e', 'l', 'l', 'o', '!']
>>> foo.remove("l")
>>> foo
['h', 'e', 'l', 'o', '!']
```

PA MOGU DA SA `insert` DA UNESEM NESTO ISPRED NEKOG INDEKSA

```py
>>> foo.insert(2, "l")
>>> foo
['h', 'e', 'l', 'l', 'o', '!']
```

## DA SE PODSETINM SORTINGA IN PLACE

```py
>>> my_list = [2, 1, 16, 8, 4]
>>> my_list.sort(reverse = True)
>>> my_list
[16, 8, 4, 2, 1]
```

## A OVO JE KRIRANJE SORTED KOPIJE BEZ MUTATINGA ORIGINAL LISTE

MOGU TO URAITI NA KOMPLIKOVANIJI NACIN KRIRANJEM POTPUNO NOVE LISTE

```py
>>> other_list = []
>>> other_list.extend(my_list)
>>> other_list
[16, 8, 4, 2, 1]
>>> other_list.sort()
>>> other_list
[1, 2, 4, 8, 16] 
```

ILI SA `sorted` GLOBALOM

```py
>>> neu_list = sorted( other_list, reverse = True)
>>> neu_list
[16, 8, 4, 2, 1]
>>> 
```

# DA SE PODSETIM `in`; ON FUKCIONISE I ZA SET I ZA LIST I ZA DICTIONARY

```py
>>> foo = ['h', 'a', 'me']
>>> bar = {"tool": "stuff"}
>>> my_set = {'Stavros', 'Adam', 'Nick'}

>>> "a" in foo
True
>>> "tool" in bar
True
>>> "Adam" in my_set
True
```

# SADA CU DA SE BAVIM SA `set`

OPET TE PODSECAM DA ZA KREIRANJE PRAZNOG SETA MORAS KORISTITI METODU, JER AKO KORISTIS BRACKETS NAPRAVICES PRAZAN DICTIONARY

NAPRAVICU SADA PRAZAN SET PA CU MU NESTO DODATI

```py
>>> my_set = set()
>>> my_set.add("Stavros")
>>> my_set
{'Stavros'}
```

```py
>>> my_set.add("Nick")
>>> my_set.add("Adam")
>>> my_set
{'Stavros', 'Adam', 'Nick'}
```

SADA CU NESTO UKLONITI IZ TOG SET-A







