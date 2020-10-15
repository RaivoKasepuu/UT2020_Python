"""
Kontrollülesanne 6.1 - Tervitused (tähtaeg 21. okt. (incl))
Tähtaeg: kolmapäev, 21. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö


Väiksematel üritustel on külaliste ühekaupa tervitamine lihtne. Suurematel üritustel võib ühekaupa tervitamine olla
juba kurnavam tegevus. Ülesanne on esmalt koostada ilma argumentideta funktsioon tervitus(), mis kuvab väljakutsel
ekraanile täpselt sellisel kujul tervituse ja vastuse.

Võõrustaja: "Tere!"
Külaline: "Tere, suur tänu kutse eest!"

Seejärel koostada programm, mis

küsib kasutajalt külaliste arvu;
rakendab tsükli abil vastav arv kordi funktsiooni tervitus().
Funktsiooni kirjelduses tsüklit pole. Küll aga funktsiooni ennast rakendatakse tsükli kehas.

Vihje: kuidas saab sõne sees jutumärke kasutada?

NB! Funktsiooni nimi peab olema täpselt see, mis on ülesandes ette antud.

"""
def tervitus():
    print('Võõrustaja: "Tere"')
    print('Külaline: "Tere, suur tänu kutse eest!"')


visitors = int(input("Sisesta külaliste arv: "))
for i in range(visitors):
    tervitus()
