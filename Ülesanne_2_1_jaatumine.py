#Kontrollülesanne 2.1 - Jäätumine (tähtaeg 23. sept. (incl))"""
"""
Tähtaeg: kolmapäev, 23. september 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
 

Mitmed autod hoiatavad võimaliku jää eest, kui temperatuur õues on 4,0 või alla selle.

Koostada programm, mis

küsib kasutajalt õhutemperatuuri,
väljastab ekraanile Ei ole jäätumise ohtu, kui sisestatu on üle 4,0,
väljastab On jäätumise oht, kui temperatuur on 4,0 või alla selle.
Temperatuuri võib sisestada nii täisarvuna kui ka ujukomaarvuna, nt -1.3.

Näited programmi tööst:
"""
print("Sisesta õhutemperatuur")
temp = float(input())
if temp > 4 :
    print("Ei ole jäätumise ohtu")
else :
    print("on jäätumise oht")