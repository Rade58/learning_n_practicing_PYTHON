# PRACTICING DATA TYPES; AND USING `print()`

NAJBOLJ BI BILO DA SVE ISCITAS IZ OVE SEKCIJE 2, KOJA GOVORI O DATA TYPES, I DA POCNES DA VEZBAS

EVO NEKIH ZADATAKA

### IZRRACUNAJ RENT PER DAY, AKO ZNAS MONTHLY RENT

```py
>>> rent = 8000
>>> rent_per_day = rent / 30
>>> rent_per_day
266.6666666666667
```

# `print()` MI NE ZNACI MNOGO U REPL-U

**ALI KADA BUDEM PISAO PROGRAME U FAJLOVIMA, I KADA IH RUNN-UJEM AGAINST EXECUTABLE, JEDINO CU UZ POMOC OVOG PRINTINGA ZNATI, KOJU VREDNOST HOLD-UJE NEKA VARIJABLA**

DAKLE PRINT JE POPUT `console.log` IZ JAVASCRIPT-A; A MOGUCE MU JE DODAVATI I VISE ARGUMENATA

```py
>>> one = "Thousand"
>>> two = "Island"
>>> three = "Stare"
>>> print(one, two, three )
# ZANIMLJIVO JE TO DA CE EMPTY SPACES BITI UMETNUTA U KONACNI STRING
Thousand Island Stare
```