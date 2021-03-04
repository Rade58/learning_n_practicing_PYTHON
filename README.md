# INCREMENT I DECREMENT

POTPUNO SAM NEKOKO U PROSLIM PRIMERIMA ZAOBISAO DA OVO MOGU RADITI; IAKO SAM J KORISTIO VALIDNU SINTAKSU ASSIGNMENTA, SAMO STO SAM TADA KORISTUI DUZU SINTAKSU

NAIME TREBALO JE DA UPOTREBIM `counter += broj` ILI `counter -= broj` UMESTO ONOG DUZEG BPISANJA `counter = counter + broj` ILI `counter = counter - broj`

EVO NAJBOLJE CES VIDETI IZ PRIMERA

```py
>>> count = 0
>>> while count < 4:
...     print(count)
...     count += 1
... 
0
1
2
3



>>> counter = 10
>>> while True:
...     print(counter)
...     if counter == 4:
...             break
...     counter -= 2
... 
10
8
6
4

```

MISLIM DA JE OVO SUVISNO OBJASNJAVATI

