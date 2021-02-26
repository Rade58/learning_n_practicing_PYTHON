# PRACTICING FUNCTIONS

## ZA prvu VEZBU CU KREIRTI BASIC FUNCTION ZA DODAVANJE BROJEVA, ODNOSNO ZA SUMU; PA CU ONDA DA JE POZIVAM

```py
>>> def add_numbers(x,y):
...     return x + y
... 
>>> 
>>> foo = 4
>>> baz = 6
>>> add_numbers(2,8)
10
>>> add_numbers(foo, baz)
10
>>> 
```

# OPET TI GOVORIM DA OBRACIS PANJU NA SCOPE, KOJI SE U PYTHONU ODREDJUJE INDENTATION-OM

AKO NE DODAS INDENTATION IMACES INDENTATION ERROR

```py
def bar():
... x = 4
  File "<stdin>", line 2
    x = 4
    ^
IndentationError: expected an indented block
```

LJUDI VOLE PYTHON I ZBOG OVIH ERROR MESSAGE-OVA KOJE SU TOKOM NAPREDOVANJA JEZIKA POSTALE EVEN SIMPLER, I MORE DESCRIPTIVE

# OPET TI SKRECEM PAZNJU I NA ONAJ ERROR KOJI SAM SPOMENUO, A KOJI SE TICE KORISCENJA VARIJABLE, PRE NJENE DEKLARACIJE

```py
>>> name = "Johny"
>>> def foo():
...     print(f"My friend {name}") # TI VEROVATNO MISLIS DA JE OVO name IZ SPOLASNJEG OBIMA (ALI NIJE TAKO)
...     name = "Billy"
... 
>>> foo()

# I ZATO IMAS ERROR JER JE U FUNKCIJINOM OBIMU VEC BILO name

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'name' referenced before assignment
>>> 
```

**NARAVNO AKO IMAS PARAMETRE KOJI IMAJU ISTA IMENA KAO NESTO IZ SPOLJASNJEG OBIM, JASNO JE DA CE SE U FUNKCIJI KORISTITI PARAMETRI KADA IH REFERENCIRAS** (TO SAM MOZDA PROPUSTIO DA KAZEM)

```py
>>> x = "Billy"
>>> y = "Ted"
>>> def foo(x, y):
...     print(f"My friends {x} and {y}")
... 
>>> foo("Kevin", "Nick")
My friends Kevin and Nick
>>> print(f"My friends {x} and {y}")
My friends Billy and Ted
```

MISLIM DA JE KOMENTAR SUVISAN, SVE JE JASNO
