# `pass` KEYWORD

OVAJ KEYWORD SLUZI KAO PLACEHOLDER ZA FUTURE CODE

KADA SE OVAJ KEYWORD EXECUTE-UJE NISTA SE NE DOGADJA

**USTVARI, OVO CE SPRECITI ERROR: 'empty code is not allowed'**

- `touch foobaz.py`

```py
print("foobarbaz")

if True:

    # OVO CE SIGURNO IZAZVATI ERROR, JER IMAS
    # PRAZAN OBIM
```

RUN-OVAO SAM FILE I DOBIO ERROR

```js
line 4
    
            ^
SyntaxError: unexpected EOF while parsing
```

## PORAVICU GORNJI CODE SA `pass`

```py
print("foobarbaz")

if True:
    pass

```

SADA KADA RUN-UJEM FILE NECE DOCI DO ERROR-A

```js
foobarbaz
```

A KASNIJE KADA DODJE VREME TI MOZES DA pass ZAMENIS CODE

A SIGURAN SI DA NECE DOCI DO ERROR-A
