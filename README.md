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


