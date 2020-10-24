"""
Kontrollülesanne 7.2 - Päevik (tähtaeg 28.okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Inimesed on ikka päevikut pidanud - mõned salaja, mõned avalikult. Ülesandeks on päevikupidamise programm teha.

Kirjutada programm, mis

küsib kasutaja käest ühe sissekande (võib eeldada, et sissekanne on ilma reavahetusteta);
kirjutab (UTF-8 kodeeringus) faili paevik.txt lõppu kolm rida:
esimesel real praegune kuupäev ja kellaaeg sellisel kujul, nagu seda tagastab funktsioon datetime.today() (vt näidet);
teisel real kasutaja sisestatud kirje;
tühi rida (pole kohustuslik).
Kui faili paevik.txt ei eksisteeri, siis tuleb see luua. Kui aga fail juba eksisteerib, siis ei tohi selle faili
olemasolevast sisust midagi üle kirjutada. Failinimi peab automaatkontrolli läbimiseks kindlasti olema paevik.txt
(mitte päevik.txt) ja fail peab olema kodeeringus UTF-8 (encoding="UTF-8").

Praeguse kuupäeva ja kellaaja saamisel aitab järgmine programmilõik.

from datetime import datetime
kuupäev_kellaeg = datetime.today()
print("Kuupäev ja kellaeg: " + str(kuupäev_kellaeg))
Näide programmi tööst:

"""
from datetime import datetime
timeStamp = "Kuupäev ja kellaeg: " + str( datetime.today()) + str(" \n")
inputString = input("Sisesta sissekande tekst: ")
inputString += str(" \n")
emptyLine = str(" \n")
inputArray = [timeStamp, inputString, emptyLine]
file = open("paevik.txt", "a", encoding="UTF-8")
file.writelines(inputArray)
file.close()
