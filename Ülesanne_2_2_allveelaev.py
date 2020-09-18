# Kontrollülesanne 2.2 - Allveelaev (tähtaeg 23. sept. (incl))
"""
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Teemapargis on allveelaeva atraktsioon, kuhu pääsevad ainult inimesed, kes on lühemad kui 120 cm. Lisaks peab atraktsioonile pääsemiseks omama piletit või kaelakaarti.

Koostada programm, milles

küsitakse tema pikkust sentimeetrites,
küsitakse, kas kasutaja omab kaelakaarti (kasutaja sisestab jah või ei),
küsitakse, kas kasutaja omab piletit (kasutaja sisestab jah või ei),
väljastatakse ekraanile Pääseb allveelaevale, kui kasutaja pääseb atraktsioonile, vastasel juhul väljastatakse Ei pääse allveelaevale.
Proovige kirjutada programmi kasutades ainult ühte tingimuslauset (aga kui ei õnnestu, siis võib ka mitmega).
"""

print("Sisesta pikkus [cm]: ")
pikkus = float(input())
print("Kas kasutaja omab kaelakaarti [jah/ei] ?")
kaelakaart = input()
print("Kas kasutaja omab piletit [jah/ei] ?")
pilet = input()
if (pikkus < 120) and (kaelakaart == "jah" or pilet == "jah"):
   print ("Pääseb allveelaevale")
else:
   print("Ei pääse allveelaevale")
      