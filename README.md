# COMPARING ZERO `0` WITH `False`; AND COPARING `1` WITH True 

***

digresija:

**OVO JE POTPUNO ISTO I U JAVASCRIPT-U**

***

KADA COMPARE-UJES `0` SA `False`, KORISCENJEM `==` DOBICES `True`

```py
>>> 0 == False
True

>>> 0 >= False
True

>>> 0 <= False
True
>>> 
```

KADA COMPARE-UJES `1` SA `True`, KORISCENJEM `==` DOBICES `True`

```py
>>> 1 == True
True

>>> 1 >= True
True

>>> 1 <= True
True
```

# A ZATO JE TAKO ?

ZATO STO:

**UNDER THE HOOD `True` JESTE `1`**

I

**UNDER THE HOOD `False` JESTE `0`**

A OVO TI TO NAJLAKSE DOKAZUJE

```py
>>> True > False
True
>>> False < True
True
```

## TAKO JE BILO I U JAVASCRIPT-U

SAMO I DIDN'T BOTHER TO CHECK

## ZAPAMTI, OVO NE VAZI ZA DRUGE FALSY ILI TRUTHY VREDNOSTI

A S OBZIROMM STA ZNAS TO NIJE NI LOGICNO DA BUDE

```py
>>> "" == False
False
>>> 8 == True
False
```

