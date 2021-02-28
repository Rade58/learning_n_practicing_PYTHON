# SETOVI

PREDVIDJENI SU ZA STORING IMMUTABLE TYPE-OVA IN AN UNSORTED WAY

ITEMI SE STAVLJAJU U CURLY BRACKETS I ODVOJENI SU ZAREZOM

**SAME (ISTI) ITEM MOZE SE POJAVITI U SETU SAMO JEDNOM; DUPLIKATI NISU DOZVOLJENI**

**NECES MOCI KORISTITI INDES DA ACCESS-UJES ITEM, ODNOSNO ITEM-E NE MOZES ACCESS-OVATI BY POSITION; JER POSITION NE POSTOJI; ODNOSNO SET DOESN'T HAVE ORDER TO IT**

# BENEFIT SET-A JE VERY FAST MEMBERSHIP TESTING

ODNOSNO NECE SE MORATI CHECK-OVATI SVI DA SE PRONADJE KONKETAN ITEM

SET KINDA STORE-UJE HASHED VALUE TIPA SVOG ITEM-AS

**SVE U SVEMU, CHECKING DA LI JE NEKI ITEM, DEO NEKOG SET-A, JE VEOMA VEMO FAST OPERATION, JER NE MORAS DA EXAMINE-UJES EACH ITEM**

# ZA ONE KOJI IMAJU MATH BACKGROUND, BICE AMAZING STO NA SETU MOZES DA PRIMENJUJES POWERFUL OPERATIONS

TU SU **UNIONS**, **DIFERENCE** AND **INTERSECTIONS**

# MORAS VODITI RACUNA O TOME DA NE MOZES TEK TAKO NAPRAVITI EMPTY SET

OVO NECE BITI EMPTY SET

```py
>>> foo = {}
>>> type(foo)
# TO JE EMPTY DICTIONARY
<class 'dict'>
>>> 
```

**DA NAPRAVIS EMPTY SET, MOZES RADITI OVO**

```py
>>> my_empty_set = set({})
>>> type(my_empty_set)
<class 'set'>
```

**ILI OVO**

```py
>>> my_empty_set_2 = set()
>>> type(my_empty_set_2)
<class 'set'>
```

`DAKLE TRICKY JE TO STO CURLY BRACKETS KORISTE I SETS I DICTIONARIES`

AKO NE MOZES DA ZAPAMTIS OVE STVARI

CAK I EXPERIANCED PYTHON DEVELOPERS STALNO KORISTE REPL I KORISTE TAMO `type` `help` `dir`

AUTOR WORKSHOPA STALNO KORISTI REPLE TO TEST HER ASUMPTIONS

MOZDA NIJE TEMA DA OVO SADA KEM, ALI POSTOJE I DRUGI REPLOVI SA SYNTAX HIGHLIGHTINGOM I MNOGIM DRUGIM POMAGALIMA

**SVE U SVEMU REPL JE SUPER POWERFUL TOOL ZA PYTHON PROGRAMERS**

**NE ZABOAVI DA KORISTIS type IF YOU ARE NOT SURE ABOUT SOMETHING**

# POKAZACU TI SADA TO DA SET-OVI NE MOGU DA CONTAIN-UJU DUPLICATES; ALI I TO DA NECES DOBITI ERROR AKO POKUSAS DA DODAS DUPLICATE

```py
>>> foo = {"Kevin", "Zoro", "Kevin"}
>>> foo
{'Zoro', 'Kevin'}
```

# MOZES PROVERITI LENGTH TVOG SET-A

```py
>>> len(foo)
2
```

# SET-OVI NE MOGU CONTAIN-OVATI MUTABLES

```py
>>> bar = {1,2, [1,2]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
KAO STO VIDIS DOBIO SAM ERROR JER SAM POKUSAO DA DODAM LIST, A TO JE MUTABLE

# SVAKI IMMUTABLE IMA HASH I TI, NECES, SKORO UOPSTE TOKOM RADA KORISTITI HASH FUNKCIJU DA PROVERIS KOJI JE HASH NECEGA

ALI ZNAJ DA POSTOJI HASH FUKCIJA I SADA CU JE ISPROBATI

```py
>>> hash(8)
8
>>> hash("Rade")
2136358387914788546
```

**POKUSAJ DA DOBIJES HASH NECEGA STO JE MUTABLE**

```py
>>> hash([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list' 
```

*KAO STO VIDIS DOBIO SI ERROR*

# ISTI TYPE ERROR, KOJI JE IZNAD DOBICES I KADA POKUSAS DA STAVIS MUTABLE U SET

```py
>>> {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

**DAKLE OPET NAPOMINJEM DA SET MOZE SAMO HOLD-OVATI IMMUTABLE TYPE**

# SET-OVI SE MOGU KORISTITI KAU UTILITY AKO ZELIS DA DEDUP-UJES (DEDUPLICATE-UJEES) LISTU

```py
>>> my_list = [1,2,2,4,4,4,4,5,5,8]
>>> deduped = set(my_list)
>>> deduped
{1, 2, 4, 5, 8}
>>> 
```
