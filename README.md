# `keys` `values` `items`

***

digresija1:

**KLJUCEVE DICTIONARY-JA, MISLIM SAMO NA KLJUCEVE, TREBA POSMATRATI KAO SET**

**NEMA DUPLIKATA U KLJUCEVIMA, ZATO TI TO GOVORIM**

VIDECES ZASTO SAM TI TO REKAO

digresija2:

**NE MORAS STALNO KORISTITI NAZIV: "KEY/VALUE" PAIR, DOVOLJNO JE DA KAZES "ITEM"**

***

## `keys` METODA RETURN-UJE SET KLJUCEVA

POSTO NE SME BITI KEY DUPLIKATA, LOGICNO JE DA OVA METODA RETURN-UJE ONO STA SAM REKAO

```py
>>> foo = {8: "Something", "baz": "Nick", "bar": ["John", "Gong", 16]}
>>> keys = foo.keys()
>>> keys
# MEDJUTIM OVO MI VISE LICI NA LIST UMESTO NA SET
# MEDJUTIM KAKO GOD OKRENES TO JE NIZ UNIQUE VREDNOSTI
dict_keys([8, 'baz', 'bar'])
# IPAK JE RETURNED, NEKAKAV SPECIFICAN TYPE, KOJI VEROVATNO IMA OSOBINE SET-A
>>> type(keys)
<class 'dict_keys'>
# MEDJUTIM OVAJ TYPE IMA NEKE KORISNE METODE
>>> dir(keys)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__rsub__',
```

KAO STO VIDIS NA POMENUTOM OBJEKTU SU METODE, KOJE SE MOGU UPOTREBLJAVATI 

## `values` METODA RETURN-UJE LISTU VALUE-OVA

RETURN-UJE LISTU, JER PO LOGICI POSTO MOZE BITI DUPLIKATA, U POGLEDU VALUE-OVA; LOICNO JE DA METODA BUDE LISTA, JER ONA MOZE IMATI DUPLICATES

```py
>>> values = foo.values()
>>> values
dict_values(['Something', 'Nick', ['John', 'Gong', 16]])
# I OVO JE NEKI SPECIAL TYPE
>>> type(values)
<class 'dict_values'>
# A EVO VIDIS KAKVE METODE IMA
>>> dir(values)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

## `items` METODA RETURN-UJE SET TUPLE-OVA

KORISNA METODA ZA UNPACKING, JEDNOG DICTIONARY-JA

POTPUNO JE LOGICNO DA TO BUDE SET TUPLE-OVA

JER SVAKI ITEM (SVAKI KEY VALUE PAIR JE UNIQUE PO SVOJOJ PRIRODI)

```py
>>> items = foo.items()
>>> items
# OVO ZAISTA LICI NA LISTU TUPLE-OVA, VISE NEGO NA SET TUPLE-OVA
# ALI PO LOGICI, IPAK SU SVI TI TUPLE-OVI UNIQUE I NEMA VEZE DA LI JE REC O SETU ILI LISTI
dict_items([(8, 'Something'), ('baz', 'Nick'), ('bar', ['John', 'Gong', 16])])
# ALI KAO STO SAM REKAO ZA OSTALE, MOZDA JE TO NEKAKAV SPECIJALNI TIP, USTVARI ON TO I JESTE
>>> type(items)
<class 'dict_items'>
>>> dir(items)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'isdisjoint']
```

