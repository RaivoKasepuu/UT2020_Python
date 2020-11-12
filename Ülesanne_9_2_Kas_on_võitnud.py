"""
Kas on võitnud? (tähtaeg 11. november (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnevatele funktsioonidele antakse argumendiks 5 x 5 tabel, milles iga element on kas täisarv lõigust 1 - 75 või
täht X. Täht X sümboliseerib seda, et vastav arv on juba loositud.

1. Koostada funktsioon võitis_nurkademängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud
nurkademängu.

2. Koostada funktsioon võitis_diagonaalidemängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on
võitnud diagonaalidemängu. Selleks koostada ja kasutada kahte abifunktsiooni:

Funktsioon x_peadiagonaalil, mis tagastab antud tabeli peadiagonaalil olevate X arvu.
Funktsioon x_kõrvaldiagonaalil, mis tagastab antud tabeli kõrvaldiagonaalil olevate X arvu.
3. Koostada funktsioon võitis_täismängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud
täismängu.
"""

def võitis_nurkademängu(tabel):
    if tabel[0][0] == "X" and tabel[0][4] == "X" and tabel[4][4] == "X" and tabel[4][0] == "X":
        return True
    else:
        return False

def x_peadiagonaalil(tabel):
    d = 0
    for i in range(5):
        if tabel[i][i] == "X":
            d += 1
    return d


def x_kõrvaldiagonaalil(tabel):
    d = 0
    for i in range(5):
        if tabel[i][-1-i] == "X":
            d += 1
    return d


def võitis_diagonaalidemängu(tabel):
    if x_peadiagonaalil(tabel) == 5 and x_kõrvaldiagonaalil(tabel) == 5:
        return True
    else:
        return False

def võitis_täismängu(tabel):

    q = 0
    for j in range(5):
        for i in range(5):
            if tabel[i][j] == "X":
                q += 1
    if q == 25:
        return True
    else:
        return False
