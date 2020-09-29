"""
Kontrollülesanne 3.4b - Vabavisked (tähtaeg 30.sept.(incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Kolmest ülesandest (3.4a, 3.4b, 3.4c) tuleb lahendada vähemalt üks, max punktideks kõik kolm.

Korvpalluri vabavisete senist visketabavust saab (teatud mööndustega) kasutada tuleviku visete tõenäosusena.

Koostada programm, mis

küsib kasutajalt visketabavuse (tabavustõenäosuse) protsentides (täisarv 0 kuni 100);
simuleerib while-tsükli abil 1000 viset ja igal viskel (arvestades tõenäosust) väljastab, kas see tabas;
iga viske kohta peab väljastama ühe rea ja see rida peab sisaldama sõna tabas või mööda
arvutab kokku tabanud visete arvu ja see väljastab selle kõige viimasena.
"""
from random import randint
print("Sisestage visketabavuse protsent: ")
visketabavusProtsent = int(input())
viskeid = 1000
vise = 1
tabas = 0
while vise <= 1000:
    if randint(1, 100) <= visketabavusProtsent:
        print(str(vise)+". vise tabas")
        tabas += 1
    else:
        print(str(vise) + ". vise mööda")
    vise += 1
print("Tabas " + str(tabas) + " viset.")
