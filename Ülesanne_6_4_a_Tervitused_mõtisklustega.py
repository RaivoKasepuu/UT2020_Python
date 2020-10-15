"""
Kontrollülesanne 6.4a - Tervitused mõtisklustega (tähtaeg 21. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Muuta ülesandes 6.1 koostatud programmi nii, et tervitamisel lisatakse ka, mitmes tervitus käsil on. Selleks tuleb
funktsioonile tervitus lisada argument, seda funktsioonis sobivalt kasutada ja igal tsükli sammul tuleb funktsioon välja
kutsuda ühe võrra suurema argumendiga kui eelmisel korral.
"""

def tervitus(counter):
    print('Võõrustaja: "Tere"')
    print("Täna on " + str(counter + 1) + ".kord tervitada, mõtiskleb võõrustaja.")
    print('Külaline: "Tere, suur tänu kutse eest!"')


visitors = int(input("Sisesta külaliste arv: "))
for i in range(visitors):
    tervitus(i)
