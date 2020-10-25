"""
Kontrollülesanne 5.4a - Reisidiilid (tähtaeg 14. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Ada tahab minna reisile ja uurib viimase hetke pakkumisi. Võimalikud sihtkohad on kirjas failis (iga sihtkoht on eraldi
real). Faili võite salvestada siit või koostada ise mõne tekstiredaktoriga.

Koostada programm, mis

küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt sihtkohad.txt);
loeb sisestatud nimega failist andmed;
näitab kõik sihtkohad koos järjekorranumbritega (alates 1);
küsib kasutajalt, mitmes sihtkoht broneerida (kasutaja sisestab alati täisarvu);
väljastab ekraanile vastavalt valitud arvule sihtkoha.
Näide programmi tööst:

Näiteks antud näitefaili sihtkohad.txt puhul peab ekraanile ilmuma
"""

sisendfail = input("Palun sisestage failinimi: ")
fail = open(sisendfail, encoding="UTF-8")
sihtkohad = []
for rida in fail:
       sihtkohad.append(rida)
fail.close()
for i in range(len(sihtkohad)):
    print(str(i + 1) + ". " + str(sihtkohad[i]))
valik = int(input("Mitmes sihtkoht broneerida? [ number vahemikus 1..." + str(len(sihtkohad)) + " ] "))
if valik > len(sihtkohad) or valik < 1:
    print("Sisestatud valik on väljaspool etteantud piire. Head aega!")
else:
    print("Reis on broneeritud. Sihtkoht " + str(sihtkohad[valik - 1]))
