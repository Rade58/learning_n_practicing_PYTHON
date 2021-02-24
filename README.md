# NUMBERS

## Integers

OVO SU SVE INTIGERS

```py
>>> x = 8
>>> y = -288
>>> z = 0 
```

## Floats

```py
>>> i = 8.0
>>> j = -288.48
>>> k = 0.0
```

### MOZES DA IH SADA PROVERIS U REPLU I VIDIS DA SU ONI BROJEVI ZISTA FLOATS, BEZ OBZIRA STO SI STAVIO SAMO POINT ZERO

```py
>>> i
8.0
>>> type(i)
<class 'float'>

# moguc je reassignment

i = -1
>>> type(i)
# VIDIS SADA JE int
<class 'int'>
```

# COMPLEX NUMBERS CE TE ZANIMATI SAMO AKO RADIS MATHY STUFF

OVO JE NA PRIMER KOMPLEKSAN BROJ

```py
>>> foo = 42j

>>> type(foo)
<class 'complex'>
```

AKO NE RADIM NISTA MATHY DA SE TAKO IZRAZIM, NECU MORATI DA KORISTIM KOMPLEKSNE BROJEVE

# BROJEVI SU UNDER THE HOOD USTVARI OBJEKTI TAKO I DA TU MOGU ZVATI METODE

```py
>>> foo = 8.0
>>> dir(foo)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```

EVO DA ISPROBAM JEDNU

```py
>>> bar = -8.0
>>> rounded = bar.__round__()

>>> rounded
-8

>>> bar
-8.0
>>> 
```

# ZATO STO SU U PITANJU OBJEKTI MOZES DA PRAVIS I `int` I `float` INSTANCE

```py
>>> baz = int(8)
>>> bar = float(-8.0)
>>> yota = float('8')


>>> baz
8
>>> bar
-8.0
>>> yota
8


>>> type(baz)
<class 'int'>

>>> type(bar)
<class 'float'>

>>> type(yota)
<class 'int'>
```

# MOGU RADITI I MATEMATICKE OPERACIJE KAO STO SU OVE

```py
>>> num_1 = -4.2
>>> num_2 = 4

>>> num_2 + num_1
-0.20000000000000018

```

# S OBZIROM DA JE DIVISON BY ZERO USTVARI INFINITY I DA NE POSTOJI TAJ TYPE, DOBICES ERROR

```py
>>> 2 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

# KADA DEVIDE-UJES DVA BROJA, IAKO TI JE DELJENIK INTEGER, I AKO TI JE DELILAC INTEGER; I AKO BI TREBALO DA DOBIJES CEO BROJ, TI CES IPAK DOBITI (DOT ZERO) FLOATING POINT

```py
>>> 4/2
2.0

```
