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

# ALI IMAS I BACKLASH (`\`) NA RASPOLAGANJU

SADA CE SVE BITI OK

```py
>>> 'You\'re Splinter'
"You're Splinter"

```