# REMOVING ITEMS FROM A LIST

POSTOJI I NEKOLIKO NACINA DA SE REMOVE-UJE ITEM FROM A LIST

## MOGUCE JE KORISTITI `list.remove`

OVO UKLANJA FIRST OCCURANCE OF THE VALUE

```py
>>> my_list = [1,2,3,4,5,6,4,8]
>>> my_list.remove(4)
>>> my_list
[1, 2, 3, 5, 6, 4, 8]
```

EVO UKLONIO SAM BROJ 4, I TO SAMO FIRST OCCURANCE OF 4

**ISTO TAKO VIDIM DA SA OVOM METODOM NIJE MOGUCE UKLONITI SECOND OCCURANCE AKO BI ON POSTOJAO**

NIJE MOGUCE, KAO SA DRUGIM METODAMA DA SE ZDAJE RANGE ODAKLE SE SERCH-UJE ILI DA SE KRENE OD NAZAD
