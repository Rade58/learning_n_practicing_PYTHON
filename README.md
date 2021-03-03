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
Stavros
34
18000
Metal
```
