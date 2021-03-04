# `return` STATEMENT INSIDE LOOP

AKO IMAS FUNKCIJU I U NJOJ LOOP, I AKO UPOTREBIS return INSIDE LOOP, TO CE NARAVNO PREKINUTI LOOP JER JE SAM FUNKCIJA ISTO RETURNED, ODNONO I ONA CE PRESTATI SA RADOM

```py
>>> def foo():
...     count = 8
...     while True:
...             print(count)
...             count -= 1
...             if count == 4:
...                     return
... 
>>> foo()
8
7
6
5
```

KAO STO VIDIS return STATEMENT JE ZAISTA ESCAPE-OVAO LOOP
