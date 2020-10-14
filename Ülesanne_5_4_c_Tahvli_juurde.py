"""
Kontrollülesanne 5.4c - Tahvli juurde (tähtaeg 14. okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Mõned õpetajad on tavatsenud õpilasi tahvli juurde vastama kutsuda kuupäeva järgi vastavalt õpilaste nimekirjale.
Näiteks 4. kuupäeval tuleb esimesena vastama nimekirjas 4. olev õpilane. Failis nimekiri.txt on õpilaste nimed,
igaüks eraldi real. Üks selline, mis on genereeritud leheküljel http://random-name-generator.info/, on siin.
Võite ise koostada ka teistsuguse nimekirja.

Koostada programm, mis

küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal on vähemalt 31 nime);
loeb sisestatud nimega failist andmed;
väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema.
Programm peab tänase kuupäeva leidma automaatselt, aluseks saab võtta järgmise näite:

from datetime import *
print(datetime.now().day)

"""
from datetime import *
sisendfail = input("Palun sisestage failinimi: ")
fail = open(sisendfail, encoding="UTF-8")
nimekiri = []
for rida in fail:
       nimekiri.append(rida)
fail.close()
print("Vastama tuleb: " + str(nimekiri[datetime.now().day - 1]))

