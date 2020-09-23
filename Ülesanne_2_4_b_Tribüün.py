# Kontrollülesanne 2.4b - Tribüün
"""
Vabaõhuetendusel saavad vaatajad istuda põhja- või lõunatribüünil. Pileti ostmisel küsitakse kõigepealt,
kas inimene tahab ise valida kummal tribüünil ta istub või see loositakse. Kui inimene tahab ise valida,
siis järgmisena küsitakse, kas põhja- või lõunatribüünil. Kui ta ei taha valida, siis loositakse tribüün nii,
et 2/3 tõenäosusega on see põhjatribüün ja 1/3 tõenäosusega lõunatribüün.

Koostada programm, mis järgib ülaltoodud tingimusi ja väljastab ekraanile, millisele tribüünile istuda ja kas
valik oli tahtlik või loosiga.

Kui kasutaja valis tribüüni ise, siis tuleb väljastada Valisite ise, vastasel juhul Pilet loositi.
Kui kasutaja soovib ise tribüüni valida, siis kirjutab ta esimesele küsimusele vastuseks ise, kui soovib loosida,
siis kirjutab midagi muud.
Kui kasutaja soovib valida põhjatribüüni, siis kirjutab ta vastuseks p ja kui soovib lõunatribüüni, siis kirjutab
ta midagi muud.

Lahendus peab (korrektselt) kasutama funktsiooni randint() moodulist random.


"""
import random
print('Kui soovite ise valida kummal tribüünil istuda, siis sisestade "ise": ')
valik = input()
if valik == "ise":
    print('Kui soovite põhjatribüünile, siis sisetage "p": ')
    tribuun = input()
    if tribuun == "p":
        print("valisite ise. Pilet on põhjatribüünile")
    else:
        print("valisite ise. Pilet on lõunatribüünile")


else:
    loos = random.randint(1, 3)
    if loos == 1:
        print("Pilet loositi. Pilet on lõunatribüünile")
    else:
        print("Pilet loositi. Pilet on põhjatribüünile")
