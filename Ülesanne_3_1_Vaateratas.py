"""
Kontrollülesanne 3.1 - Vaateratas (tähtaeg 30.sept.(incl))
Tähtaeg: kolmapäev, 30. september 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Linnas on vaateratas, mille kõige kõrgemast asendist näeb tervet linna. Vaateratas teeb teatud arvu ringe.

Koostada programm, mis

küsib kasutajalt, mitu ringi vaateratas teeb ning
väljastab sama arv kordi ekraanile Näen tervet linna!.
"""

ringideArv = int(input("Sisesta, mitu ringi teeb vaateratas: "))
while ringideArv > 0:
    print("Näen tervet linna!")
    ringideArv -= 1
