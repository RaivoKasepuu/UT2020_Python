"""
Kontrollülesanne 7.4b - Nimepäev (tähtaeg 28.okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Kui aadressile https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/ lisada kuunimi (nt.
https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/jaanuar), siis sellelt aadressilt võib leida lehe, kus on
kirjas selle kuu nimepäevalised nii, et igal real on ühe päeva nimepäevalised (esimesel real on selle kuu esimese päeva
nimepäevalised, teisel real on selle kuu teise päeva nimepäevalised jne.). "märts" asemel tuleb kasutada ilma
täpitähtedeta versiooni "marts".

NB! Kui ülaltoodud aadressilt andmeid ei saa kätte (nt Macide kasutajad), siis palun proovida
http://kodu.ut.ee/~eno/mooc/jaanuar jt.

Kirjutada programm, mis

küsib kasutajalt kuunime (võib eeldada, et kasutaja sisestab kuunime õigesti ja "märts" asemel kirjutab "marts"),
küsib kasutajalt päeva (võib eeldada, et sisestatud kuus leidub sellise järjekorranumbriga päev),
loeb vastavalt aadressilt selle kuu nimepäevad (kasulik oleks nendest koostada järjend, abiks võib olla meetod
splitlines()) ja
väljastab ekraanile sisestatud kuupäevale vastavad nimepäevalised.
"""
from urllib.request import urlopen
month = input("Sisestage kuu: ")
day = int(input("Sisestage päev: "))
FileName = "https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/" + month
fileFromWeb = urlopen(FileName)
bytes = fileFromWeb.read()
text = bytes.decode()  # baitidest saab sõne
byRow = text.splitlines()  # sõne jaotatakse reavahetuse kohtadelt
fileFromWeb.close()
print("Kuupäeval " + str(day) + ". " + str(month) + " on nimepäevad järgmistel inimestel: ")
print(str(byRow[day - 1]))
