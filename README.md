# ADDING ITEMS TO A LIST

KAO STO VIDIS OVDE SAM DODAO ITEM, NA KRAJ LISTE KORISCENJEM `append` METODE

```py
>>> my_list = [1, 2, 4]
# EVO OVDE APPEND-UJEM KORISCENJEM METODE
>>> my_list.append(8)
>>> my_list
[1, 2, 4, 8]

```

## insert

**MEDJUTIM POSTOJI JOS NACINA ZA DODAVANJE ITEMA**

MOGUCE JE INSERT-OVATI ISPRED NEKOG INDEXA

*EVO OVDE SAM INSERT-OVAO 8 ISPRED DRUGOG INDEKSA*

*STO ZNACI DA CE TO INSERTED 8 IMATI INDEX 2*

```py
>>> my_list.insert(2,8)
>>> my_list
[1, 2, 8, 4, 6, 8]
```

KAO STO VIDIS OVO JE KORISNO JER SAM INSERT-OVAO ITEM NA ARBITRARY POSITION

## KOMBINOVANJE DVE LISTE TOGETHER (CONCATENATION OF LISTS)

**TADA KORISTIM** `extend` METODU

```py
>>> list_a = ["something", "anything"]
>>> list_b = ["foobars", "bazisms"]
>>> list_a.extend(list_b)
>>> list_a
['something', 'anything', 'foobars', 'bazisms']
```

EVO KAO STO VIDIS EXTEND-OVAO SAM ILI CONCATENATE-OVAO SAM PRVU LISTU SA KOPIJOM DRUGE

JER DRUGA LISTA JE I DALJE ONAKVAA KAKVA JE BILA

```py
>>> list_b
['foobars', 'bazisms']
```
