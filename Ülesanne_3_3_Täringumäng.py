"""
Kontrollülesanne 3.3 - Täringumäng (tähtaeg 30.sept.(incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut.

Koostada programm, mis

küsib kasutajalt vajalike täringute arvu;
viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
väljastab iga arvu eraldi reale.
Vihje: kui kasutada tsüklit, mis teeb kasutaja sisestatud arvu samme, siis igal sammul tuleb genereerida üks juhuslik arv ja see väljastada.
"""
from random import randint
diceCount = int(input("Täringute arv: "))
while diceCount > 0:
    print(randint(1, 6))
    diceCount -= 1
