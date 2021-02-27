# LISTS

DAKLE SADA CU GOVORITI OD ADVANCED DATA TYPES; ODNOSNO O **`ADVANCED CONTAINER TYPES`**, A LISTE SU JEDAN OD TIH TYPE-OVA

**U PITANJU SU `CONTAINERS OBJECT` KOJI MI POMAZU DA ORGANIZUJEMO DATA U ONE DATA STRUCTURE, ODNOSNO U KOLEKCIJE SA KOJIMA MOZEMO LATER RADITI**

## CHEATSHEET

IMAS GA OVDE:

<https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/10-lists/#list-cheat-sheet>

TU MOZES VIDETI, MOST IMPORTANT INFORMATIONS

# JA SAM RANJE VEC NA JEDAN NACIN PRAVIO LIST

EVO NEKOLIKO LISTA

```py
>>> []
[]
>>> [1,2,3,4]
[1, 2, 3, 4]
```

# TAKODJE MOGUCE JE KORISTITI METODU KOJA PRAVI LIST

```py
>>> list()
[]
>>> list([8,6,4,8])
[8, 6, 4, 8]
>>> list("nesto")
['n', 'e', 's', 't', 'o']
>>> list("12345678")
['1', '2', '3', '4', '5', '6', '7', '8']
```

VIDIS KAKVE SU SVE MOGUCNOSTI OVE BIUILT IN METODE IZ GORNJEG PRIMERA

# A DA POTVRDIS O TOME DA JE TO LIST TYPE, MOZES KORISTITI `type()` HELPER

```py
>>> type([])
<class 'list'>
```

# LITE IMAJU USEFUL METHODS ALI ONE NISU ON THEM, KAKAV JE SLUCAJ BIO SA ONIM METODAMA KOJE SE PRIMENJUJU NA PRIMITIVS IMA, POPUT STRING-OVA I BROJEVA

EVO NA PRIMER, LENGTH LISTE BI UZIMAO TAKO STO, KORISTIM `len` METHOD

```py
>>> my_list = [1,2,3,4]
>>> len(my_list)
4
```

ALI KAKO VIDIM, IPAK MOGU DA NADJEM NEKE METODE NA LISTI; MOZDA JE REC O NEKIM SHORTHAND-OVIMA, KOJI USTVARI KORISTE TE 'STANDALONE' GLOBALNE BUILT IN METODE

TO JE METODA ILI ACCESS-OR, KOJI KORISTI UNDERSCORE SINTAKSU

```py
>>> my_list.__len__()
4
```

NARAVNO ZA OVU GORNJU METODU SAM SAZNAO KORISTECI `dir` METODU A I `help` METODU

```py
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
```

DOBRO HELP MI NIJE BAS REKAO MNOGO ALI MI JE STAMPAO CELU METODU

```py
>>> help(my_list.__len__)
# DA TI NE POKAZUJEM STA JE STAMPANO, JER I NIJE BILO BAS HELPFUL
# ALI SVE JE INTUITIVNO
```

# OVA `len` METODA SE MOZE KORISTITI I NA STRING-OVIMA

```py
>>> len("My name is Josef")
16
```

# TAKODJE I SET-OVI I DICTIONARIS SE MOGU KORISTITI SA `len`

ALI O TOME CU GOVORITI KADA SE BUDEM BAVIO, POMENUTIM TYPE-OVIMA

# LISTA RETAIN-UJE ORDER OF THEIR ITEMS

DAKLE KAKO SI IH LAY-OVAO DOWN U LISTU, ITEMI CE CE IMATI TAKVE INDEKSE

NARAVNO, ISTI DATA TYPE KAO I Array FROM JAVASCRIPT

```py
>>> my_list = ["a", "b", "c", "d"]
>>> my_list[0]
'a'
```

MISLIM DA JE OVDE, GORE SVE JASNO JASNO

# A AKO POKUSAS DA PRISTUPIS NEPOSTOJECEM CLANU, DESICE SE, OPET NESTO PO CEMU SE PYTHON RAZLIKUJE OD JAVASCRIPT-A

```py
>>> my_list = [1,2,3,4]
>>> my_list[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

KAO STO VIDIS OVDE IMAS INDEX ERROR DOK BI U JAVAASCRIPT-U, TO UPRVO BILO `undefined`

DAKLE U PYTHONU O OVOME MORAM DA VODIM RACUNA POSEBNO,, ZA RAZLIKU OD JAVASCRIPT-A

# PROBAO SAM I DA KORISTIM NEGATIVAN INDEKS PRI PRISTUPANJU; I TADA CES SE IZNENADITI JER CES VIDETI NESTO LEPO

A TO JE DA SE CLANOVIMA SA NEGATIVNIM BROJEVIMA USTVARI PRISTUPA OD KRAJA

VIDIS NA STA MISLIM

```py

```