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
