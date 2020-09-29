"""
Kontrollülesanne 3.4c - Male (tähtaeg 30.sept.(incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Kolmest ülesandest (3.4a, 3.4b, 3.4c) tuleb lahendada vähemalt üks, max punktideks kõik kolm.

Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu. (Sellest legendist räägib ka Tõnu Tõnso paarikümne aasta taguses leheloos.)

Leiutaja oli “tagasihoidlik” ja palus tasuks

esimese ruudu eest 1 nisutera,
teise ruudu eest 2 korda rohkem ehk 2,
kolmanda ruudu eest veel 2 korda rohkem ehk 4,
neljanda ruudu eest siis 8,
viienda ruudu eest 16 jne
Malelaual on 64 ruutu.

Koostada programm, mis

küsib kasutajalt ühe täisarvu;
arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu eest leiutaja küsis;
tulemus väljastatakse ekraanile pärast tsüklit.
"""

base = int(input("Sisestage täisarv: "))
astendaja = 1
nisuteri = 1
while astendaja < base:
    nisuteri *= 2
    astendaja += 1
print("Nisuteri " + str(base) + ". ruudu eest: " + str(nisuteri))
