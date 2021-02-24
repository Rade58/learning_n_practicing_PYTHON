# REPL

REPL ZNACI: "READ EVAL PRINT LOOP"

KAO STO NODEjs IMA REPL KOJI SE POKRECE SA `node`, AKO SE SECAS, TAKO POSTOJI I REPL KOJI SE KORISTI ZA PYTHON

DAKLE OVO CE MI OMOGUCITI DA IMAM DIREKTNU INTERAKCIJU SA PYTHON ITERPRETER-OM

# REPL OTVARAM ISTO PREKO KOMANDE KOJU MOGU PRONACI SA COMMAND LISTE

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

PA BIRAM `Python: Start REPL`

## POSTO SI POKRENUO REPL, JSNO JE DA CE ON BITI OTVOREN U INSTANCI TERMINALA U VSCODE-U

MOZES TAMO DA TYPE-UJES DA VIDIS KAKO STVARI FUNKCIONISU

MOZES DA SABERES DVA BROJA I INSTANTNO DA VIDIS REZULTAT

**DAKLE TVOJ REPL PROPMPT JE OTVOREN I ON JE PREDSTAVLJEN SA TRI LARGER THAN (`>>>`)**

# DEKLARISACU SVOJU PRVU VARIJABLU

```py
>>> name = "Rade"
```

SADA KADA KUCAS VARIJABLU `name` BICE OUTPUTED NJENA VREDNOST

# TRI VEOMA VEOMA IMPORTANT METODE KOJE CU KORISTITI TOKOM OVOG UPOZNAVANJA

## 1) `type()`

AKO ZELIS DA NAS TYPE NECEGA, TO CES KORISTITI

```py
>>> type(name)
<class 'str'>
```

## 2) `dir()`

AKO ZELIS DA VIDIS KOJE METODE IMA AVAILABLE NEKI TYPE, USTVARI BILO STA STO SI DEKLARISAO; **E PA OVA METODA CE TI IZLISTATI SVE**

RECIMO AKO PROSLEDIM MOJU VARIJABLU JA CU SAZNATI, KOJE SVE METODE IMA NJEN TYPE, A TO JE `'str'` TYPE

```py
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

**HANDY STVAR AKO ZABORAVIM, KOJE METODE SE MOGU PRIMENJIATI NA INSTANCI NEKOG TIPA**

ISPROBACU NEKU OD METODA, NA PRIMER OVAKO

```py
>>> name.upper()
```

JASNO TI JE STA CE SE DOBITI

A FUNKCIONISE I AUTOCOMPLETE NA TAB

## 3) `help()`

AKO SE OSECAS IZGUBLJENO POKRENES OVU KOMANDU; ODNOSNO AKO NE ZNAS STA METODA RADI

MOZES PASS-OVATI, NEKI TYPE, ILI NEKU METODU NEKOG TYPE-A NA SLEDECI NACIN

```py
>>> help(str.upper)

Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.
```

ALI TI TO MOZES RADITI IZBOROM METODE SA VARIJABLE

```py
>>> help(name.upper)
```

I OVO GORE CE TI DATI OBJASNJENJE

**EVO KAKVO OBJASNJENJE CU IMATI ZA NEKI TYPE**

PASS-OVACU `str` TYPE (USTVARI str GLOBAL, AKO MOGU TTTAK ODA SE IZRAZIM)

```py
>>> help(str)

Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
```

DAKL `str` JE KLASA

