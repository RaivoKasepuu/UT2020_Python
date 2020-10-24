"""
Kontrollülesanne 7.1 - Telegramm (tähtaeg 28.okt. (incl))
Tähtaeg: kolmapäev, 28. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Aastakümneid oli telegramm infovahetamisel väga olulisel kohal. Telegrammiga teatati saabumistest, õnnitleti jpm.
Praeguseks on telegrammid paljudes maades (ka Eestis) ajalukku jäänud ja teisteski kasutatakse neid järjest vähem.
Noorem generatsioon pole telegrammidega tõenäoliselt üldse kokku puutunud ja ka vanemad ei mõtle telegrammidele eriti
sageli. Muuseumides ja ajalooblogides võib ühtteist siiski leida. Ilmselt on telegramme ka kodustes arhiivides.

Telegrammis kasutati ainult suurtähti. Täpitähti kasutada ei saanud ja nii oli Ä asemel kasutusel AE, Õ ja Ö asemel OE
ja Ü asemel UE.

Palju õnne sünnipäevaks

asemel oli kirjas

PALJU OENNE SUENNIPAEVAKS

Olgu (UTF-8 kodeeringus) failis sõnum, mis on kirjutatud tavalisel moel.

Kirjutada programm, mis

küsib kasutajalt failinime,
loeb vastavast failist sõnumi ja
väljastab selle ekraanile telegrammi stiilis. Teha tuleb asendused
Ä, ä → AE
Õ, õ, Ö, ö → OE
Ü, ü → UE
Kõik tähed tuleb muuta suurtähtedeks.
Teisi märke ei muudeta.
Näide programmi tööst:
"""
telegram = ""
inputFile = input("Palun sisestage failinimi: ")
file = open(inputFile, encoding="UTF-8")
# if from web:
# bytes = file.read()
# text = bytes.decode()
# print(text)

# if from text:
for row in file:
    for char in row:
        if char == "Ä" or char == "ä":
            telegram += "AE"
        elif char == "Õ" or char == "õ" or char == "Ö" or char == "ö":
            telegram += "OE"
        elif char == "Ü" or char == "ü":
            telegram += "UE"
        else:
            telegram += char.upper()
file.close()
print(telegram)

