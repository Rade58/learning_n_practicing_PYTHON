# LOOPING OVER DICTIONARIES

KADA POKUSAS DA LOOP-UJES KROZ DICTIONARY VARIJABLA LOOP-A CE HOLD-OVATI CURRENT KEY U SVAKOJ ITERACIJI

EVO POGLEDAJ

```py
>>> my_dict = {"name": "Stavros", "age": 34, "welth": 18000, "music": "Metal"}
>>> for kljuc in my_dict:
...     print(kljuc)
...     print(my_dict[kljuc])
... 
name
Stavros
age
34
welth
18000
music
Metal
```

KAO STO VIDIS GORE, JA SAM STAMPAO CURRENT KEY, ALI SAM ISKORISTIO CURRENT KEY DA ACCESS-UJEM I VALUE-U I TO SAM STAMPAO

# ALI JA MOGU DA LOOP-UJE I KROZ CELE ITEMS, KORISCENJEM `items` METODE; ILI MOGU DA LOOP-UJEM KROZ VALUES, KORISCENJEM `values` METODE

EVO LOOP-UJEM KROZ ITEMS

```py
>>> for item in my_dict.items():
...     print(item)
...
# IMAM TUPLE SATAVLJEN OD KEY-A I VALUE-A U SVAKOJ ITERACIJI 
('name', 'Stavros')
('age', 34)
('welth', 18000)
('music', 'Metal')
```

LOOP-UJEM KROZ VALUES

```py
>>> for value in my_dict.values():
...     print(value)
...
# U SVAKOJ ITERACIJI STMAPAN JE CURRENT VALU
Stavros
34
18000
Metal
```

# MOGUCE JE UNPACK-OVATI TUPLE U SVAKOJ ITERCIJI

```py
>>> for label, val in my_dict.items():
...     print(label)
...     print(val)
... 
name
Stavros
age
34
welth
18000
music
Metal
```

S OBZIROM DA SU VARIJABLE U OJEM SAM UNPACK-OVAO TUPLE USTVARI GLOBALNE, I NISU SCOPED TO FOR LOOP, JER REKAO SAM TI VEC DA LOOP NEMA SVOJ SCOPE

I S OBZIROM DA JE U POSLEDNJOJ ITERACIJI, KLJUC BIO "music", A VALUE BILA "Metal"; VARIJABLE BI TREBALE DA IMAJU TE VREDNOSTI

TO CU I PROVERITI

```py
>>> label
'music'
>>> val
'Metal'
```
