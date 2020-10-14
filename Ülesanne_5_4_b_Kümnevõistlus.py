"""
Kontrollülesanne 5.4b - Kümnevõistlus (tähtaeg 14. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Noor mitmevõistleja on sel aastal kümnevõistluse läbinud kaks korda ja alade kaupa saadud punktid on järjendites:
käärikul = [401, 604, 547, 700, 722, 845, 621, 490, 800, 700] ja
kohilas = [900, 0, 333, 803, 838, 400, 467, 488, 432, 700].

Koostada programm, mis

koostab nende järjendite põhjal paremate tulemuste järjendi, milles igale kohale võetakse vastav parem tulemus
(näitejärjendite puhul algab paremate tulemuste järjend [900, 604 ... );
väljastab ekraanile paremate tulemuste järjendi ja paremate tulemuste järjendi elementide summa.
NB! Programm peab töötama kõikide seesuguste täisaarvujärjenditega, mis on pikkusega 10.
"""
käärikul = [401, 604, 547, 700, 722, 845, 621, 490, 800, 700]
kohilas = [900, 0, 333, 803, 838, 400, 467, 488, 432, 700]
best = käärikul
max = 0
for i in range(len(käärikul)):
    if käärikul[i] >= kohilas[i]:
        best[i] = käärikul[i]
        max += käärikul[i]
    else:
        best[i] = kohilas[i]
        max += kohilas[i]
print(best)
print("summa: " + str(max))
