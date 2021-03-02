# BOOLEAN LOGIC

RANIJE SAM TI, NAKRATKO POKAZAO BOOLEANS, USTVARI MOZDA SAM IH SE SAMO MALO DOTAKAO

IMAS DVA BUILT IN-A, A TO SU `True` I `False`

```py
>>> a = False
>>> b = True
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
```

EVO KAKVE SVE STVARI NA SEBI IMA `bool` TYPE

```py
>>> dir(bool)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

MEDJUTIM JA NISAM GOVORIO O TRUTHY I FALSY VREDNOSTIMA

# TRUTHINESS

KADA PRAVIS BOOLEAN TI MOZES PROVERAVATI I DA LI JE NEKI VALUE TRUTHY, KORISCENJEM `bool`

MOZES I OVAKO PRAVITI BOOLEAN STO SIGURNO OBICNO NE BI RADIO

```py
>>> bool(True)
True
>>> bool(1)
True
>>> 
```

ALI KAO STO VIDIS, DOBAR JE ZA IGRANJE U REPLU, U CILJU PROVERE DA LI JE NESTO TRUTHY ILI NE

