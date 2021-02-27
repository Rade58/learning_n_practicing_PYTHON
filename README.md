# TUPLES

LIGHT WIGHT COLLECTIONS, GENERALNO SE KORISTE ZA KEEP TRACK OF RELATED BUT DIFFERENT ITEMS (TAKO SE KORISTE U PRAKSI BUT YOU ARE FREE TO DO WHAT YOU WANT)

**ZA RAZLIKU OD LISTI, TUPLES SU `IMMUTABLE`**

KADA SE KREIRA TUPLE, ITEMS IN IT CAN'T BE CHANGED

KORISNI SU ZA TAKING A SNAPSHOT OF DATA

# DA NAPRAVIS TUPLE, OPCIONO KORISTIS OBICNE ZAGRADE (PARENTHESIS), A U ZAGRADAM ITEME ODVAJAS ZAREZIMA

KASNIJE CU TI RECI ZASTO SAM REKAO "`OPCIONO`"

EVO NAPRAVICU EMPTY TUPLE

```py
>>> a = ()
>>> type(a)
<class 'tuple'>

```

OVO ZNACI TAKODJE DA SE TUPLE MOZE BRAVITI I SA `tuple` KLASOM

MEDJUTIM TUPLE IMA NEKOLIKO GOTCHAS

# AKO BEZ RAZMISLJANJA POKUSAS DA NAPRAVIS TUPLE SA JEDNIM CLANOM, ON TI IZ JEDNOG RAZLOGA, MOZDA NECE BITI tuple TYPE, VEC TYPE-A ONOG SVOG JEDINOG CLANA

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

POSTOJI MOGUCNOST DA SE PREDHODNO PREVAZIDJE AKO ZELIS TUPLE SA JEDNIM CLANOM

## PREDHODNO SE DOGODILO JER TUPLES NISU SAMO PRANTHESIS I U NJIMA NESTO, VEC SU `GLAVNA STVAR U NJIMA, UPRAVO COMMAS` (ZAREZI)

KOMBINACCIJA OPCIONIH ZAGRADA I COMMAS

PO TOME I OVO BI BIO TUPLE

```py
>>> foo = 1,2
>>> type(foo)
<class 'tuple'> 
```

I ZAISTA TO JE BIO TUPLE

**KAO STO SAM POMENUO, TUPLE SE MOZE, ZISTA NAPRAVITI TAKVIM DA IMA JEDAN CLAN, A TO CU TI POKAZATI KADA NESTOO SUMIRAM**

# ZNACI, O SADA SAM REKAO DA ZA PRAVLJENJE EMPTY TUPLE-A TREBAJU TI ZGRADE; A ZA TUPLE SA DVA ILI VISE CLANOVA, ZAGRADE SU OPCIONA STVAR

```py
>>> foo = ()
>>> bar = 1,2,3,4
>>> baz = (4, 8, 6, 12)
>>> type(foo)
<class 'tuple'>
>>> type(bar)
<class 'tuple'>
>>> type(baz)
<class 'tuple'>
```

DAKLE COMMA JE MORE IMPORTANT PART OF PARENTHESIS

# MEDJUTIM MOZES DA NAPRAVIS "TRICK" DA BI NAPRAVIO TUPLE SA JEDNIM CLANOM

TO SAM JA NEKAKO ZAKLJUCIO DA BI TO MOGAO URADITI STAVLJANJEM ZAREZA, (COMMA-E), NAKON SAMO TOG JEDNOG JEDINOG CLANA

EVO POGLEDAJ

```py
>>> zen = (8,)
>>> type(zen)
<class 'tuple'>

>>> blen = 6,
>>> type(blen)
<class
```

SADA IMAM TUPLE-OVE SA, PO JEDNIM CLANOM


