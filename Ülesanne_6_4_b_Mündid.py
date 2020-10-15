"""
Kontrollülesanne 6.4b - Mündid (tähtaeg 21. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Euromüntide seerias on kuus erineva nimiväärtusega senti: 1 sent, 2 senti, 5 senti, 10 senti, 20 senti, 50 senti.
Sendid väärtustega 1, 2 ja 5 on pronksikarva (vasega kaetud teras), sendid väärtustega 10, 20 ja 50 on kullakarva
(vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).

Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.

Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real. Näiteks nii:

1
20
20
5
50
2
2
1

Koostada funktsioon pronksikarva_summa, mis

võtab argumendiks täisarvude järjendi ja
tagastab selles järjendis olevate arvude 1, 2 ja 5 summa.
Koostada programm, mis

küsib kasutajalt selle faili nime, milles asuvad sentide väärtused;
moodustab täisarvujärjendi vastavast failist loetud väärtustest;
rakendab funktsiooni pronksikarva_summa, andes argumendiks koostatud täisarvujärjendi;
väljastab ekraanile tulemuseks saadud kõikide pronksikarva sentide summa.
Näide programmi tööst:

Näiteks ülaltoodud andmete korral failis nimega mündid.txt peab ekraanile ilmuma
"""
def pronksikarva_summa(coins):
    sum = 0
    for i in range(len(coins)):
        if coins[i] == 1 or coins[i] == 2 or coins[i] == 5:
            sum += coins[i]
    return sum


sisendfail = input("Palun sisestage failinimi: ")
fail = open(sisendfail, encoding="UTF-8")
coins = []
for row in fail:
       coins.append(int(row))
fail.close()

print("Hoiupõrsasse läheb: " + str(pronksikarva_summa(coins)) + " senti.")
