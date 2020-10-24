"""
Kontrollülesanne 7.4c - Elutee number (tähtaeg 28.okt. (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Numeroloogias peetakse tähtsaks elutee numbrit, mille arvutamiseks tuleb liita kokku sünnikuupäeva ja -aasta numbrid
nii, et jõutakse lõpuks ühe numbrini.

Näiteks, oletame, et sünnikuupäev on 15.05.1975. Teha tuleb niisiis järgnev tehe: 1+5+5+1+9+7+5 = 33, 3+3 = 6, seega on
elutee number 6.

Aga kui sünnikuupäevaks on nt. 17.11.1981, siis arvutada tuleb järgmiselt: 1+7+1+1+1+9+8+1 = 29, 2+9 = 11, 1+1=2.

Elutee numbrit arvutab järgmine (rekursiivne) funktsioon, mis võtab argumendiks sünnikuupäeva:

#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))
Failis sunnikuupaevad.txt on mingi hulk sünnikuupäevi, iga sünnikuupäev eraldi real. Kirjutada programm, mis tekitab
selle faili põhjal 9 tekstifaili nimedega eluteenumber1.txt, eluteenumber2.txt, ..., eluteenumber9.txt ning jagab
sünnikuupäevad nendesse failidesse vastavalt elutee numbrile (elutee numbri arvutamiseks kasutada funktsiooni elutee).
Näiteks sünnikuupäev 15.05.1975 tuleb kirjutada faili eluteenumber6.txt.

Näide programmi tööst:

Kui faili sunnikuupaevad.txt sisu on

 07.02.1969
 17.11.1981
 29.03.1955
siis faili eluteenumber7.txt sisu peab olema

 07.02.1969
 29.03.1955
ja faili eluteenumber2.txt sisu peab olema

 17.11.1981
Kõik ülejäänud 7 faili peavad selle näite korral küll tekkima, aga jääma tühjaks.
"""