# CHANGING ORDER OF A LIST

## SADA CU D SORT-UJEM LIST

```py
>>> my_list = [6, 2, 81, 8]
# DA VIDIM PRVO KOJE METODE MOGU PRIMENITI
>>> dir(my_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# MPOGU PRIMENITI sort
>>> my_list.sort()
>>> my_list
[2, 6, 8, 81]

# NIJE KREIRANA NOVA LISTA KOJA JE KOPIJA STARE SAMO SORTED, VEC JE DAKLE
# LISTA SORTED, STO MOZES I SAM PRIMETITI
```

KAO STO VIDIS SORT-OVAO SAM LIST

MEDJUTIM POSTOJI I BUILT IN GLOBALNA `sorted` METODA

**ALI OVA METODA PRAVI POTPUNO NOVU LISTU STO SAM I PROVERIO**

```py
>>> list_a = [8, 12 ,2, 4, 1, 8]
>>> list_b = sorted(list_a)
>>> list_b
[1, 2, 4, 8, 8, 12]
# VEC CE TI OVDE BITI JASNO DA JE IZNAD REC O POTPUNO NOVOJ LISTI
>>> list_a
[8, 12, 2, 4, 1, 8]
# ALI EVO DA POTVRDIM JOS VISE
>>> list_b == list_a
False
>>> 
```

DAKLE OVA METODA JE KREIRALA POTPUNO NOVU LISTU

I ONE IMAJU JOS ARGUMENATAI OBE METODE SAM PROVERIO SA `help()`

```py

help(sorted)

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.


>>> help(list.sort)

sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.


```

## MOGUC JE SORTING U REVERSE STRANU

```py
>>> cool_list = [8, 2, 1, 12, 4]
>>> cool_list.sort(reverse = True)
>>> cool_list
[12, 8, 4, 2, 1]
```

EVO KAO STO VIDIS SAMO JER SAM ZADA O KEYBOARD ARGUMENT, JA SAM USPEO DA SORT-UJEM LIST REVERSELY

ISTO MOZES SORT-OVATI SA `sorted` GLOBAL METODOM, SAMO STO TADA DODAJES I POSITIONAL ARGUMANT, A TO JE LISTA, PA TEK ONDA KEYBOARD ARGUMENT, A TO JE ONAJ KOJI UKAZUJE NA REVERSE SORTING

# KADA PRIMANJUJES NEKU METODU NA ISTI, NEKA TI BUDE JASNO DA CE TA METODA VEROVATNO MODIFIKOVATI LISTU NA KOJU METODU PRIMNJUJES

TAKVA JE METODA `list.sort()`

A ONE METODE KOJE SU GLOBALI, KAO STO JE `sorted` PRAVICE, POTPUNO NOVU LISTU

# POSTOJI METODA KOJA CE SAMO REVERSOVATI ORDER LISTE

NECE JE SORT-OVATI, NARAVNO

```py
>>> my_list = [8, 1, 0, 2, 6]
>>> my_list.reverse()
>>> my_list
[6, 2, 0, 1, 8]
```

I KAO STO VIDIS LISTA JE ZAISTA REVERSOVANA

# EVO TI NEKI PROCES PO KOJEM TI SAZNAJES KAKVE SVE METODE MOZES KORISTITI SA LISTOM

```py
# IMAS TVOJ DATASET
>>> my_list = [8,4,5,1]
# PROVERIS KOJEG JE ON TIPA
>>> type(my_list)
<class 'list'>
```

ONDA POGLEDAS KAKVE SU SVE METODE VEZANE ZA NJEGA

```py
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

MADA SI U `dir` MOGAO DA PROSLEDIS I SAMU LISTU (my_list)

METODE KOJE SU BEZ UNDERSCORE-A, CE BITI GENERALNO METODE ZA KOJE CARE-UJEM ABOUT

I ONDA AKO ZABORAVIS KOJA METODA KORISTI KAKVE ARGUMENTE, ISTO MOZES KORISTITI `help()`

```py
>> help(list.reverse)
reverse(self, /)
    Reverse *IN PLACE*.
```

KAO STO VIDIS RECENO TI JE DA METODA REVERSE-UJE IN PLACE; ODNOSNO DA REVERSUJE ITEME, MENJAJUCI ORDER U LISTI; NE PRAVI NOVU LISTU