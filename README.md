# del KEYWORD

PROPRILICNO JE INTUITIVO

```py
>>> foo = ["h", "i", "i", "a", "m", "me"]
>>> del foo[2]
>>> foo
['h', 'i', 'a', 'm', 'me']
```

KAO STO VIDIS UKLONIO SAM ITEM KOJI JE IMAO INDEX 2, IZ MOJE LISTE

MISLIM DA SAM VEC RANIJE KORISTIO .remove METODU

ALI UPOTREBICU JE JOS JEDNOM, **I KOD NJE SE NE KORISTE INDEX VEC VALUE**

```py
>>> foo.remove("i")
>>> foo
['h', 'a', 'm', 'me']
>>> 
```

# MEDJUTIM del SE MOZE KORISTITI I NA DICTIONARY-JU

```py
>>> bar = {2: 8, "some": True}
>>> bar
{2: 8, 'some': True}
>>> del bar[2]
>>> bar
{'some': True}
```


