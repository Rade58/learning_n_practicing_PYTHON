# DAKLE MOGUCE JE RESTRUKTURIRATI LISTU, ODNOSNO KAKO SE TO U PYTHON TERMINOLOGIJU, 'UNPACK'-OVATI LISTU

**UNPACKING LISTE SE RETKO KORISTI; NAJVISE SE KORISTI UNPACKING TUPLE-A**

ALI EVO POKAZACU TI KAKO DA UNPACK-UJES LIST

```py
>>> my_list = ["Bulding", "Mike", 8]
# EVO OVAKO UNPACK-UJM
>>> place, name, amount = my_list
# IMAM SADA DOSTUPNE VARIJABLE
>>> place
'Bulding'
>>> name
'Mike'
>>> amount
8
>>> 
```

## ALI GOTCHA JE STO MORAS UNPACK-OVATI CELU LISTU

```py
>>> foo = ["Kenny", 8, "New York"]
# LIST IMA TRI ITEMA A JA SAMO POKUSAVAM DA UNPACK-UJEM DVA
>>> baz, bar = foo
# I IMAM ERROR, ZBOG TOGA
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> 
```

