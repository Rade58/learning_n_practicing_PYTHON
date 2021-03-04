# `while` LOOP AND CONTROL STATEMENTS

NISAM SE DO SADA BAVIO DO SADA SA while LOOP-OM U PYTHON

POPRILICNO MI JE INTUITICNO KAKO CE IZGLEDATI OVAJ LOOP

**U OVOM LOOP-U MOGU KORISTITI `continue` I `break` KEYWORD-OVE**

`continue` SLUZI DA SE PREKINE CURRENT ITERACIJA I DA SE ODMAH KRENE SA SLEDECOM

`break` SLUZI DA SE POTPUNO ESCAPE-UJE LOOP

# EVO JEDAN while LOOP BEZ POMENUTIH KEYWORD-OVA

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

# `continue` AND `break`

VEC SAM IH OBJASNIO, ALI SADA HAJDE DA IH ISPROBAM

```py
# IMAM DVA COUNTA
>>> count_1 = 0
>>> count_2 = 9
# IMAM ENDLESS LOOP, JER CE CONDITION UVEK BITI TRUE
>>> while True:
        # OVO CE BITI ISPUNJNO SVE DOK COUNT 1 NE PORASTE
...     if count_1 < 5:
...             print(f"count_1 --> {count_1}")
...             count_1 = count_1 + 1
                # OVO JE DAKLE JEEDNA OD BITNIJIH STVARI JER JE
                # PRESKOCENO SVE ISPOD continue DA BI SE PRESLO U NAREDNU ITERACIJU
...             continue
        # POSTO GORNJA USLOVNA IZJAVA KRENE DA EVALUATE-UJE TO FALSE OVO SLEDECE CE SE IZVRSVATI
...     print(f"count_2 --> {count_2}")
...     count_2 = count_2 - 0.5
        # SVE DOK DRUGI COUNT NE PADNE DO NULA
        # LOOP CE RADITI
        # I KADA COUNT2 BUDE 0 A KADA SE ISPRED
        # 0 STAVI not TO SE EVALUATE-UJE TO False
        # ONDA CE SE ONO UUNDER USLOVNE IZJAVE IZVRSITI
...     if not count_2:
                # A TO JE BREAKING , ODNOSNO ESCAPING FROM THE LOOP
...             break
... 
# UPRAVO JE SVE ZATO OVAKO STAMPANO
count_1 --> 0
count_1 --> 1
count_1 --> 2
count_1 --> 3
count_1 --> 4
count_2 --> 9
count_2 --> 8.5
count_2 --> 8.0
count_2 --> 7.5
count_2 --> 7.0
count_2 --> 6.5
count_2 --> 6.0
count_2 --> 5.5
count_2 --> 5.0
count_2 --> 4.5
count_2 --> 4.0
count_2 --> 3.5
count_2 --> 3.0
count_2 --> 2.5
count_2 --> 2.0
count_2 --> 1.5
count_2 --> 1.0
count_2 --> 0.5
```

MISLIM DA JE SVE JASNO

# POMENUTI KEYWORD-OVI SE MOGU KORISTITI I SA `for` LOOP-OVIMA

POGLEDAJ OVO

```py
>>> names = ["Kevin", "Tim", "Kelly", "Stavros", "Jonthan", "Sally", "Emillia", "Henrik"]
>>> for name in names:
...     print(f"name --> {name}")
...     if name == "Sally":
...             break
... 
name --> Kevin
name --> Tim
name --> Kelly
name --> Stavros
name --> Jonthan
name --> Sally 
```

I OVO JE SASVIM JASNO; SAVIM JE JASNO GDE SAM PREKINUO LOOP I KADA SE PRESTALO SA LOOPING THROUGH LIST

## U WORKSHOP WEBSITE0U POTOJI I HELPFUL VIZUALIZACIJA

IAKO MI JE JASNO IPAK CU OSTAVITI LINK

<https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/#break-and-continue-visualized>
