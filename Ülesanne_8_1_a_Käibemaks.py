"""
Kontrollülesanne 8.1a (tähtaeg 11.nov. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Väga paljudes riikides on kehtestatud käibemaks. Eestis on see paljude kaupade puhul 20%, mis tähendab, et kui näiteks
ilma käibemaksuta hind on 500 eurot, siis käibemaksuga on 500 * (1 + 20/100) = 600 eurot. Teatud tingimustel saab
riigist lahkudes käibemaksu tagasi.

Mõnedes (eriti turistidele mõeldud) poodides on siltidel kaupade hinnad ilma käibemaksuta. Ada käis sellises poes ja
ostis erinevaid asju. Ta pani kirja, millised olid nende asjade hinnad poes (ehk ilma käibemaksuta). Failis on nüüd
kõik hinnad eraldi ridadel. Kui inimene lahkub riigist, siis ta saab soovi korral käibemaksu tagasi, kui konkreetse
kauba müügihind koos käibemaksuga ületab mingi taseme (nt. Euroopa Liidus 38 eurot, Tais aga 2000 bahti).

Koostada programm, mis arvutab, kui palju inimene maksis poes koos käibemaksuga. Samuti arvutab programm, kui palju ta
saab raha tagasi (kui lahkub riigist).

Koostada funktsioon hind_käibemaksuga, mis võtab argumentideks käibemaksuta hinna ja käibemaksu protsendi ning arvutab
käibemaksuga hinna ja tagastab selle. kmgaHind = kmtaHind * (1 + kmProtsent/100)

Koostada programm, mis küsib kasutajalt

failinime,
käibemaksu protsendi,
summa, millest alates saab tagasi käibemaksu.
Programm peab

lugema failist ilma käibemaksuta hinnad.
arvutama ja väljastama ekraanile koos käibemaksuga hindade summa, mis on ümardatud kahe kohani peale koma. Käibemaksuga
hindade arvutamisel kasutada funktsiooni hind_käibemaksuga.
ümardama peab tulemuse, arvutuste ajal ümardada ei tohi.
arvutama ja väljastama ekraanile, kui palju raha (ümardatuna kahe kohani pärast koma) inimene riigist lahkudes tagasi
saab. 
ümardama peab tulemuse, arvutuste ajal ümardada ei tohi.
"""
def hind_käibemaksuga(netoHind, VAT):
    return round(netoHind * (1 + VAT/100), 2)


def arve_summa(ostuList):
    total = 0
    for i in range(len(ostuList)):
        total += ostuList[i]
    return total

inputFile = input("Palun sisestage failinimi: ")
VAT = float(input("Palun sisestage käibemaksu %: "))
minTaxFree = int(input("Palun sisestage TaxFree miinimumsuma: "))
file = open(inputFile, encoding="UTF-8")
ostud = []
for row in file:
    ostud.append(float(row))
print("kokku on kulutatud: " + str(hind_käibemaksuga(arve_summa(ostud), VAT)))
overTaxFreeMin = 0
for i in range(len(ostud)):
    if hind_käibemaksuga(ostud[i], VAT) >= minTaxFree:
        overTaxFreeMin += hind_käibemaksuga(ostud[i], VAT)
print("Tagasi saab: " + str(round(overTaxFreeMin - overTaxFreeMin/(1 + VAT/100), 2)))
