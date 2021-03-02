# del KEYWORD

***

digresija

MNOGI DEVELOPERI NE VOLE DA KORISTE `del`, A MEDJU NJIMA JE I AUTOR WORKSHOP-A, KOJI RECCOMEND-UJE DA SE NE KORISTI, IAKO CES MOCI VIDETI DA GA DRUGI KORISTE

***

**POKAZACU KAKO SE OVAJ KEYWORD KOORISTI ZA LIST**

PROPRILICNO JE INTUITIVO

```py
>>> foo = ["h", "i", "i", "a", "m", "me"]
>>> del foo[2]
>>> foo
['h', 'i', 'a', 'm', 'me']
```

KAO STO VIDIS UKLONIO SAM ITEM KOJI JE IMAO INDEX 2, IZ MOJE LISTE

MISLIM DA SAM VEC RANIJE KORISTIO .remove I .pop METODE

ALI UPOTREBICU IH JOS JEDNOM 

SAMO DA, OPET KAZEM DA SU ARGUMENTI RAZLICITI ZA OVE DEVE METODE:

**KOD `remove` SE NE KORISTE INDEX VEC VALUE**
**KOD `pop` SE NE KORISTE VALUE VEC INDEX ,A MOZE I BEZ ARGUMENTA CIME SE UKLANJA POSLEDNJI ITEM**

```py
>>> foo.remove("i")
>>> foo
['h', 'a', 'm', 'me']
>>> foo.pop(-2)
'm'
>>> foo
['h', 'a', 'me']
```

# del SE MOZE KORISTITI I NA DICTIONARY-JU

```py
>>> bar = {2: 8, "some": True}
>>> bar
{2: 8, 'some': True}
>>> del bar[2]
>>> bar
{'some': True}
```


