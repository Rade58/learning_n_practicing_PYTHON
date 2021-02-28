# DODATNO

SAMO DA TI KAZEM DA SET IMA JOS MNOSTVO METODA KAO STO SU `issubset` I `issuperset`

```py
>>> set_1 = {1,2,3,4}
>>> set_2 = {3,4}
>>> set_2.issubset(set_1)
True
>>> set_1.issuperset(set_2)
True
>>> 
```

POGLEDAJ OSTALE METODE KADA BUDES IMAO VREMENA

## AKO ZELIS DA IMAS SORTED ITEME, OD NEKOG SET, MOZES KORISTITI JEDAN TRICK

ZNAS DA TI JE SET MUTABLE, ALI NMA INDEKSE I NIJE SORTABLE

E PA POSTOJI JEDAN TRICK

```py
>>> my_set = {81, 12, 4, 18 ,6}
# IDEJA JE DA SE SET KAO ARGUMENT DODA list POZIVU DA BI SE OD
# CLANOV SETA NAPRAVIO LIST
>>> my__list = list(my_set)
# ONDA GA JE LAKO SORT-OVATI
>>> my__list.sort(reverse = True)
>>> my__list
[81, 18, 12, 6, 4]
```

EVO SORT-OVAO SAM


