"""
Reeglite kontrollimine (tähtaeg 11. november (incl))
Tähtaeg: kolmapäev, 11. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Kirjutada funktsioon on_legaalne_bingo_tabel, mis võtab argumendiks 5 x 5 tabeli, milles iga element on täisarv lõigust
 1 - 75, ning tagastab tõeväärtuse vastavalt sellele, kas arvud on veergudesse jaotatud vastavalt Bingo reeglitele.

Et tegu oleks legaalse Bingo Loto mänguväljaga, peavad vasakpoolseimas veerus olema arvud lõigust 1 - 15, järgmises
veerus lõigust 16 - 30 ja nii edasi, kuni viimases veerus on arvud lõigust 61 - 75. Lihtsuse mõttes võib eeldada,
et kõik arvud on unikaalsed ehk ükski arv ei esine antud tabelis rohkem kui üks kord.

"""

def on_legaalne_bingo_tabel(table):
    result = True
    bingo = []
    for j in range(5):
        for i in range(5):
            if table[i][j] in bingo:
                return False
            else:
                bingo.append(table[i][j])
            if (j * 15 + 1) <= table[i][j] <= ((j + 1) * 15):
                continue
            else:
                result = False
    return result