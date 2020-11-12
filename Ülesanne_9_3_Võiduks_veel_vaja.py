"""
Võiduks veel vaja (tähtaeg 11. november (incl))
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnevatele funktsioonidele antakse argumendiks 5 x 5 tabel, milles iga element on kas täisarv lõigust 1 - 75 või
täht X. Täht X sümboliseerib seda, et vastav arv on juba loositud.

1. Koostada funktsioon nurkademänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud
mänguväli võidaks nurkademängu.

2. Koostada funktsioon diagonaalidemänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et
antud mänguväli võidaks diagonaalidemängu.

3. Koostada funktsioon täismänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud
mänguväli võidaks täismängu.
"""

def nurkademänguks_vaja(bingo):
    corners = []
    for i in range(0, 5, 4):
        for j in range(0, 5, 4):
            if bingo[i][j] != "X":
                corners.append(bingo[i][j])
    return corners


def diagonaalidemänguks_vaja(bingo):
    diagonal = []
    for i in range(5):
        for j in range(5):
            if (i == j and bingo[i][j] != "X") or (i + j == 4 and bingo[i][j] != "X"):
                diagonal.append(bingo[i][j])
    return diagonal


def täismänguks_vaja(bingo):
    full = []
    for i in range(5):
        for j in range(5):
            if bingo[i][j] != "X":
                full.append(bingo[i][j])
    return full
