# Kontrollülesanne 2.3 - Leedu perenimed
"""
Inimese nimede osas on erinevatel maadel erinevaid kombeid ja vähemalt naabrite puhul oleks hea neid teada (areneva Balti koostöö mõttes).

Traditsiooniliselt näitab leedu naiste perekonnanimedes nime lõpp perekonnaseisu. Näiteks on Adamkienė abielus ja Adamkutė mitte. Alates 2003. aastast on lubatud ka lühem vorm, mis perekonnaseisu ei näita, nt Adamkė. Huvi korral uuri lähemalt siit.

Koostada programm, mis küsib kasutajalt Leedu perekonnanime ja väljastab ekraanile

Abielus, kui nimi lõpeb tähtedega "ne",
Vallaline, kui nimi lõpeb tähtedega "te",
Määramata, kui nimi lõpeb tähega "e" (aga mitte "ne" ja "te"),
Pole ilmselt leedulanna perekonnanimi, kui nimi ei lõpe tähega "e".
Lihtsuse mõttes kasutame tavalist tähte "e", jätame punkti peale panemata.

Sõne nimi kahe viimase tähe kontrollimiseks saab kasutada näiteks võrdlemist nimi[-2:] == "ne". Viimase tähe kontrollimiseks sobib nimi[-1] == "e".

Näited programmi tööst:

"""
print("Sisestage Leedu perekonnanimi: ")
leeduPerenimi = input()
if leeduPerenimi[-2] == "n" and leeduPerenimi[-1] == "e":
    print("Abielus")
elif leeduPerenimi[-2] == "t" and leeduPerenimi[-1] == "e":
    print("Vallaline")
elif leeduPerenimi[-1]  == "e":
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")
