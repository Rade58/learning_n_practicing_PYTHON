# STRINGS

MOGUCE JE KORISTITI DOUBLE ILI SINGLE QUOTATION MARKS

I SAM ZNAS DA JE ZBOG APOSTROFA BOLJE KORISTITI DOUBLE QUOATATION MARKS

U REPLU MOZES VIDETI DA AKO PISES STRING SA "" DA SE ON PARSE-UJE U STRING SA ''

A LI TO NIJE SLUCAJ U STRINGU KOJI IMA QUOTATION MARKS

```py
>>> "You're ninja turtle"
"You're ninja turtle"
>>> "I am a Rat"
'I am a Rat'
```

# OVO SLEDECE CE NARAVNO DATI SYNTAX ERROR

```py
>>> 'You're Splinter'
  File "<stdin>", line 1
    'You're Splinter'
         ^
SyntaxError: invalid syntax
```

**I MISSMATCHING QUOTES CE TI DATI ERROR**

```py
>>> foo = "life is journey'
  File "<stdin>", line 1
    foo = "life is journey'
                          ^
SyntaxError: EOL while scanning string literal
# EOL znaci `end of line`
```

# IMAS I BACKLASH (`\`) NA RASPOLAGANJU

```py
>>> 'You\'re Splinter'
"You're Splinter"

```
# CONCATENATION

```py
>>> "Build " + "Programs"
'Build Programs'
```

# LONG STRING SA TRIPLE `"`

MISLIM DA SE OVO SAMO TICE REPL-A

KADA U REPLU ZELIS DA PISES DUZI TEKST KOJI SE PROTEZE PREKO VIE REDOVa, ODNOSNO DA BI IMAO MOGUCNOST DA PRITISKAS ENTER ZA NEW LINE, ZAPOCNI STRING SA TRIPLE QUOTES I UDARI ENTER; PISI U MULTIPLE REDDOVIMA UDARJUCI ENTERE NA KRAJU NAPISANOG TEKSTA I ZAVRSI POSLEDNJI RED SA TRIPLE QUOTES

VIDECES IMACS TRI DOTS NA POCETKU REDA KAD UNOSIS U REDOVE (SAMO OBJASNJAVAM)

```py
going_home = """
... looking around
... building ships'
... in the place of joy
... """

>>> going_home
# NISI MORAO DA UDARAS ENTER NKON STO NAPISES """ MOGAO SI DA PISES TEKST U NASTAVKU PA ONDA ENTER
# TO TI KAZEM ZAATO STO SADA IMAS I \n N POCETKU I KRAJU
"\nlooking around\nbuilding ships'\nin the place of joy\n"
```

# `f""` STRINGS SU NACIN DA PISES ONAKVE STRINGOVE, KAKVI SE U JAVASCRIPTU ZOVU STRING INTERPOLATION

EVO BICE TI JASNO NAKON STO OVO POGLEDAS

```py
>>> char1 = "Lando"
>>> place = "Mars"
>>> race = "Salamatrian"
>>> interpolated = f"{char1} lives on the planet {place}, a land of {race}s."
>>> interpolated
'Lando lives on the planet Mars, a land of Salamatrians.'

```

POMENUTO JE FANCY NEW STUFF IN PYTHON

JEDINO STO MORAS ZAPAMTITI DA SE KORISTIT f SA DOUBLE QUOTES I NE KORISTI SE `\``

U NEKOJ RANIJOJ SINTAKSI PYTHONA MOZES VIDETI UPOTREBU `.format` METODE, STO JE RADILO NESTO SLICNO, AL ISADA SVI KORISTE f STINGS ,MEDJUTIM MOZDA CES U NEKOJ STARIJOJ SINTAKSI NAICI NA TAJ .format

# AKO POKUAS DA CONCATANATE-UJES INTEGER I STRING ILI FLOAT I STRING, DOBICES ERROR

```py
>>> 101.8 + " dalamtians"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

**U JAVASCRIPTU JE GORE POMENUTO DOZVOLJENO**
