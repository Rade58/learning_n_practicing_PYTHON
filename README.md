# ABOUT ARGUMENTS

RANIJE SM TI POKAZAOD MOZES IMATI I DEFAULT ARGUMENTE

ALI EVO DA TI OPET POKAZEM

```py
>>> def baz(x=5):
...     return x
... 
>>> some = baz()
>>> some
5
```

U SUPROTNOM DA NEMAS DEFAULT PARAMETAR, DOBIO BY TYPE ERROR

```py
>>> def bar(x):
...     return x
... 
>>> something_else = bar()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bar() missing 1 required positional argument: 'x'
```

# ZA RAZLIKU OD JAVASCRIPTA, TI MORAS PROSLEDITI ONOLIKO ARGUMENATA KOLIKO SI PARAMETARA DEFINISAO; DAKLE SVI ARGUMENTI SU REQUIRED

```py
>>> def eksFunk(x,y):
...     return x
... 
>>> nesto = eksFunk(2,2) # OVO JE OK

# ALI CE OVO DATI ERROR
>>> blah= eksFunk(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: eksFunk() missing 1 required positional argument: 'y'
```

# POSTOJE I KEYWORD ARGUMENTS ILI KKO IH JOS NAZIVAJU kwargs; A ONI TI OMOGUCUJU DA TI PROSLEDJUJES ARGUMENTE, ONIM REDOM KOJI TI ZELIS, A NE




