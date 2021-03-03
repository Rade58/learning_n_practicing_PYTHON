# COMPARING ZERO `0` WITH `False`; AND COPARING `1` WITH True 

***

digresija:

**OVO JE POTPUNO ISTO I U JAVASCRIPT-U**

***

KADA COMPARE-UJES `0` SA `False`, KORISCENJEM `==` DOBICES `True`

```py
>>> 0 == False
True
```

KADA COMPARE-UJES `1` SA `True`, KORISCENJEM `==` DOBICES `True`

```py
>>> 1 == True
True
```

# A ZATO JE TAKO ?







## MEDJUTIM TO NE VAZI ZA DRUGE FALSY VREDNOSTI

```py
>>> "" == False
False
>>> [] == False
False
```

## I TO NE VAZI ZA COMPARING NEKE TRUTHY VREDNOSTI SA `True`

```py
>>> 8 == True
False
```


