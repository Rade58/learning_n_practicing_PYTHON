# `while` LOOP AND CONTROL STATEMENTS

NISAM SE BAVIO DO SADA SA while LOOP-OM U PYTHON

POPRILICNO MI JE INTUITICNO KAKO CE IZGLEDATI OVAJ LOOP

**U OVOM LOOP-U MOGU KORISTITI `continue` I `break` KEYWORD-OVE**

`continue` SLUZI DA SE PREKINE CURRENT ITERACIJA I DA SE ODMAH KRENE SA SLEDECOM

`break` SLUZI DA SE POTPUNO ESCAPE-UJE LOOP

# EVO JEDAN LOOP BEZ POMENUTIH KEYWORD-OVA

```py
>>> counter = 8
>>> while counter:
...     print(f"This is counter value: {counter}")
...     counter = counter - 1
... 
This is counter value: 8
This is counter value: 7
This is counter value: 6
This is counter value: 5
This is counter value: 4
This is counter value: 3
This is counter value: 2
This is counter value: 1
```

MISLIM DA OVO GORE NE MORAM POSEBNO OBJASNJAVATI

MOGU SAMO URADITI JOS JEDAN WHILE LOOP, KOJI BI MOZDA KORISTITO INKREMENTACIJU UMESTO DEKEMENTACIJE

```py
>>> while count <= max:
...     count = count + 1
...     print(f"Hello World! {count}")
... 
Hello World! 1
Hello World! 2
Hello World! 3
Hello World! 4
Hello World! 5
Hello World! 6
Hello World! 7
Hello World! 8
Hello World! 9
```

MISLIM DA JE I OVO GORE SUVISNO OBJASNJAVATI

