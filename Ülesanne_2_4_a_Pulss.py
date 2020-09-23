# Kontrollülesanne 2.4a - Pulss
"""
Kolmest ülesandest (2.4a, 2.4b, 2.4c) tuleb lahendada vähemalt üks. Maksimaalseks tulemuseks kõik kolm.

Tervisesport on tervisele kasulik, kui sellega jäädakse mõõdukuse piiridesse.
On erinevaid variante sobiva koormuse valimiseks.
Näiteks saab kasutada sellist arvestust, et maksimaalne pulsisagedus on meestel 220 miinus vanus
ja naistel 206 miinus 88% vanusest.
Seejuures erinevate treeningutüüpide puhul peaks pulsisagedus jääma järgmistesse vahemikesse:

tervisetreening 50-70% maksimaalsest pulsisagedusest,
põhivastupidavuse treening 70-80% maksimaalsest pulsisagedusest,
intensiivne aeroobne treening 80-87% maksimaalsest pulsisagedusest.
Koostada programm, mis küsib kasutajalt

vanuse (täisarvuna aastates),
soo (kasutaja sisestab M, m, N või n),
treeningu tüübi (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)
ja lõpuks väljastab pulsisageduse vahemiku vastavatel tingimustel formaadis <vähim pulss> kuni <suurim pulss>,
kus vastuses leiduvad arvud on ümardatud täisarvudeks.

Näited programmi tööst:


"""

print("Sisestage enda vanus: ")
vanus = int(input())
print( "Sisestage enda sugu: ")
sugu = input()
print("Sisestage treeningu tüüp: ")
treeninguTyyp = int(input())
if sugu == "n" or sugu == "N":
    maxPulss = 206 - 0.88 * vanus
elif sugu == "m" or sugu == "M":
    maxPulss = 220 - vanus
else:
    print("viga sisestusel")

if treeninguTyyp == 1:
    print("Pulsisagedus peaks olema vahemikus " + str(int(round(0.5 * maxPulss, 0 ))) + " kuni " + str(int(round(0.7 * maxPulss , 0))))
elif treeninguTyyp == 2:
    print("Pulsisagedus peaks olema vahemikus " + str(int(round(0.7 * maxPulss, 0))) + " kuni " + str(int(round(0.8 * maxPulss, 0))))
else:
    print("Pulsisagedus peaks olema vahemikus " + str(int(round(0.8 * maxPulss, 0))) + " kuni " + str(int(round(0.87 * maxPulss, 0))))


