"""
Kontrollülesanne 7.4a - Täiendatud peo eelarve (tähtaeg 28.okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Ülesandes 6.3 pidite kirjutama programmi, mis arvutab peo maksimaalse ja minimaalse eelarve küsides inimeste arvu
kasutajalt. Selles ülesandes tuleb inimeste arv saada failist.

Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada.

Juubelikorraldaja paneb nimekirja faili järgmisel kujul:

? Anna
+ Peeter
+ Ülle
? Eva
? Juhan
+ Maria
+ Epp
+ Anu

Faili igal real on märk + (tuleb) või ? (ei tea veel) ja inimese nimi. Tehke see fail ise mingi tekstiredaktoriga (võib
ka Thonnyga). Faili kodeeringuks kasutage UTF-8.

Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent
maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab

maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja
minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
Programmi loomisel on mõistlik aluseks võtta ülesande 6.3 lahendus, sh funktsioon eelarve, mis võtab argumendiks
külaliste arvu ning arvutab ja tagastab eelarve (10 euro iga külalise jaoks ja 55 eurot ruumi rendiks). Programm

küsib kasutajalt failinime;
loeb sellest failist informatsiooni külaliste kohta;
arvutab ja väljastab ekraanile kutsutud inimeste arvu;
arvutab ja väljastab ekraanile inimeste arvu, kes on juba tulemisest teatanud;
arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;
arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.
Näide programmi tööst:



Näiteks, kui faili nimekiri.txt sisu on ülaltoodu, siis programm peab andma tulemuse :
"""
def eelarve(visitors):
    return visitors * 10 + 55


inputFile = input("Palun sisestage külaliste faili nimi: ")
file = open(inputFile, encoding="UTF-8")
# if from web:
# bytes = file.read()
# text = bytes.decode()
# print(text)

confirmedVisitors = 0
totalNumberOfVisitors = 0

# if from text:
for row in file:
    if row[0] == "+":
       confirmedVisitors += 1
    totalNumberOfVisitors += 1
file.close()

print("Maksimaalne eelarve: " + str(eelarve(totalNumberOfVisitors)))
print("Minimaalne eelarve: " + str(eelarve(confirmedVisitors)))


