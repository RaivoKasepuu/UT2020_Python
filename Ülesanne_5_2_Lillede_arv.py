"""
Kontrollülesanne 5.2 - Lillede arv (for-tsükliga) (tähtaeg 14. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Lillepoel on sünnipäev ja pood otsustas klientidele
kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille,
neljas ei saa midagi, viies ostja saab viis lille jne.

Koostada programm, mis

küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
arvutab for-tsükli ja funktsiooni range() abil lillede koguarvu, mida pood kingib;
väljastab saadud lillede arvu ekraanile.
Vihje: lillede koguarvust võib mõelda kui summast, milles liidetavad on paaritud arvud alates 1 kuni esimese paaritu
arvuni, mis pole suurem kui klientide arv.

Näiteks, kui kasutaja sisestas 7, siis paaritute arvude summa on 16, sest 1 + 3 + 5 + 7 = 16. Kui kasutaja sisestas 8,
siis on summaks samuti 16, sest 1 + 3 + 5 + 7 = 16.

Tegemist on ülesande 3.2 variandiga for-tsükli jaoks.

Näited programmi tööst:
"""

ostjateArv = int(input("Sisesta ostjate arv: "))
lilliKokku = 0
for i in range(1, ostjateArv + 1):
    if i % 2 != 0:
        lilliKokku += i
print("Lillede koguarv on " + str(lilliKokku))

