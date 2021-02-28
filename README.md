# AKO ZELIS DATA STRUCTURE, KOJI IMA OSOBINE SETA A DA BUDE IMMUTABLE, MOZES KORISTITI FROZEN SET

```py
>>> zamrznuti_set = frozenset({"Sljiva", "Evri", "Audi", "Turbo Folk"})
>>> zamrznuti_set
frozenset({'Audi', 'Turbo Folk', 'Evri', 'Sljiva'})
>>> dir(zamrznuti_set)
# KAO STO VIDIS NEMA METODA ZA MUTATING
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

**ALI IMAS OPERACIJE (intersection, difference, union)**

STO ZNACI DA TI BUKVALNO IMAS TUPLE NA KOJEM MOZES KORISTITI POMENUTE OPERACIJE (TO JE NEKO MOJE RAZMISLJANJE)