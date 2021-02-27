# TUPLES

LIGHT WIGHT COLLECTIONS, GENERALNO SE KORISTE ZA KEEP TRACK OF RELATED BUT DIFFERENT ITEMS (TAKO SE KORISTE U PRAKSI BUT YOU ARE FREE TO DO WHAT YOU WANT)

**ZA RAZLIKU OD LISTI, TUPLES SU `IMMUTABLE`**

KADA SE KREIRA TUPLE, ITEMS IN IT CAN'T BE CHANGED

KORISNI SU ZA TAKING A SNAPSHOT OF DATA

# DA NAPRAVIS TUPLE KORISTIS OBICNE ZAGRADE (PARENTHESIS)

EVO NAPRAVICU EMPTY TUPLE

```py
>>> a = ()
>>> type(a)
<class 'tuple'>

```

OVO ZNACI TAKODJE DA SE TUPLE MOZE BRAVITI I SA `tuple` KLASOM

MEDJUTIM TUPLE IMA NEKOLIKO GOTCHAS

# AKO NAPRAVIS TUPLE SA JEDNIM CLANOM, ON NECE BITI tuple TYPE, VEC TYPE-A ONOG SVOG JEDINOG CLANA

EVO VIDI OVO

```py
>>> foo = (1.28)
>>> type(foo)
<class 'float'>
```

I KAO STO VIDIM foo CE IMATI ISTE METODE KAO STO IMA JEDAN FLOATING POINT

```py
>>> dir(foo)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```
