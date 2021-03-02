# PRACTICING ADVANCED TYPES

**PORED TOGA STO CU PROVEZBATI I PONOVITI, NEKE STVARI JA CU SAZNATI ZA NEKE 'ADVANCED' TEHNIKE (KOJIMA CU MOZDA POSVETITI NOVE BRANCHE-EVE KOJI POCINJU SA 8)**

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
>>> my_set.add("Stavros") # NEMA DUPLICATE-OVA ALI NE THROW-UJE ERROR AKO POKUSAS DA GA DODAS
>>> my_set
{'Stavros'}
```

```py
>>> my_set.add("Nick")
>>> my_set.add("Adam")
>>> my_set
{'Stavros', 'Adam', 'Nick'}
```

SADA CU NESTO UKLONITI IZ TOG SET-A (discard I remove) (JEDAN OD NJIH DAJE ERROR)

```py
>>> my_set.remove("Nick")
>>> my_set
{'Stavros', 'Adam'}

>>> my_set.discard("John")
>>> my_set.remove("John")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'John'
```

## `union` `intersection` `difference` OF A SET

```py
>>> my_set = {1,2,3,4}
>>> my_other_set = {3,4,5,6,7,8}
>>> union_set = my_set | my_other_set
>>> union_set
{1, 2, 3, 4, 5, 6, 7, 8}
>>> intersection_set = my_set & my_other_set 
>>> intersection_set
{3, 4}
>>> difference_set = my_set ^ my_other_set
>>> difference_set
{1, 2, 5, 6, 7, 8}
>>> 
```

POSTOJE I METODE SA IMANIMA KAO U NASLOVU

S TIM STO `difference` METODA IMA ONAJ QUIRK PO KOJEM SAMO VACA DIFFERENCE ZA JEDAN

# DA SE SADA BAVIM SA `tuple`

KADA PRAVIS TUPLE COMMA JE VAZN, A () SU OPCIONA STVAR

ZATO TUPLE SA JEDNIM CLANOM PRAVIM SA TRAILING COMMA

```py
>>> my_tup = 1, # DA NISI STAVIO COMM, OVO BI BIO BROJ
>>> type(my_tup)
<class 'tuple'>
```

**TUPLE-OVI SU IMMUTABLES**

**A DOBRI SU ZA UNPACKING**

```py
>>> person = ("Stavros", 24, "comedian")
>>> name, age, job = person
>>> name
'Stavros'
>>> age
24
>>> job
'comedian'
>>> 
```

## TUPLE-OVI SU ITERABLE

```py
>>> my_tuple = ("Sam", 8, True)
>>> my_tuple[0]
'Sam'
>>> my_tuple[1]
8
>>> my_tuple[2]
True
```

# DA SE SADA POZABAVIM SA `dictionary`

```py
>>> my_dict = {"name": "Nick", "age": 48}
>>> my_dict
{'name': 'Nick', 'age': 48}
```

**NEMAJU INDEKSE, ALI BROJEVI MOGU BITI KLJUCEVI**

AKO POKUSAS DA ACCESS-UJES VALUE SA NEPOSTOJECI KEY-OM DOBICES KEY ERROR

DODACU JOS PAR ITEM-A

```py
>>> my_dict[8] = "something"
>>> my_dict["amount"] = 48
>>> my_dict
{'name': 'Nick', 'age': 48, 8: 'something', 'amount': 48}
```

DA ACCESS-UJEM NESTO

```py
>>> my_dict["amount"]
48
```

AKO NESTO NEMA

```py
>>> my_dict["goat"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'goat'

# DA SE OSIGURAM DA NE DOBIJEM ERROR
>>> my_dict.get("goat") # NISTA NE VRACA, ALI BAR NEMAS ERROR

# ILI DA SE OSIGURAM DA RETURN-UJEM DEFAULT, KAD NEMA NICEGA

>>> my_dict.get("goat", "horse")
'horse'
```

## `keys` `values` `items`

OVO SU KORISNE METODE (POGLEDAJ O NJIMA OVDE: <https://github.com/Rade58/learning_n_practicing_PYTHON/tree/7_3____keys____values____items#keys-values-items> )

