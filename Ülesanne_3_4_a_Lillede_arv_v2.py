"""
Kontrollülesanne 3.4a - Lillede arv v2 (tähtaeg 30.sept.(incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Kolmest ülesandest (3.4a, 3.4b, 3.4c) tuleb lahendada vähemalt üks, max punktideks kõik kolm.

On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Üks teine lillepood on otsustanud, et nende
sünnipäeval saab iga klient kingituseks lilli nii, et esimene ostja saab ühe lille, teine ostja saab kolm lille,
kolmas ostja saab viis lille, neljas ostja seitse lille jne.

Koostada programm, mis

küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
väljastab kingitavate lillede koguarvu.
Näiteks, kui kasutaja sisestas 4, siis paaritute arvude summa on 16, sest 1 + 3 + 5 + 7 = 16. Kui kasutaja sisestas 7,
siis on summaks 49, sest 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49.
"""
print("Sisesta ostjate arv: ")
ostjateArv = int(input())
lilledeKoguarv = 0
while ostjateArv > 0:
    lilledeKoguarv +=ostjateArv*2 - 1
    ostjateArv -= 1
print("Lillede koguarv on " + str(lilledeKoguarv))
