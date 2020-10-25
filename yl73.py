"""
Kontrollülesanne 7.3 - Kalkulaator (tähtaeg 28.okt. (incl))
Nõutud failid: yl73.py (Laadi alla)
Töö liik: Individuaaltöö


Faili nimi peab olema yl73.py.

Koostada EasyGUI graafilise kasutajaliidesega kalkulaatori programm, mis

laseb kasutajal
sisestada kaks täisarvu lõigus 1-10 (integerbox);
nuppude abil valida liitmise, lahutamise või korrutamise vahel (buttonbox);
väljastab arvutuse tulemuse (msgbox).
Automaatkontrolliks peab faili nimi olema yl73.py.

"""

from easygui import *

intOne = integerbox("Int 1", lowerbound=1, upperbound=10)
intTwo = integerbox("Int 2", lowerbound=1, upperbound=10)
buttons = ["Liida", "Lahuta", "Korruta"]

vajutati = buttonbox(choices=buttons)
if vajutati == "Liida":
    msgbox("Tulemus " + str(intOne + intTwo))
if vajutati == "Lahuta":
    msgbox("Tulemus " + str(intOne - intTwo))
if vajutati == "Korruta":
    msgbox("Tulemus " + str(intOne * intTwo))
