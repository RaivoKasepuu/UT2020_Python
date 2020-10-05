"""
Kontrollülesanne 4.2b Liiklusmärk

Koostada programm, mis kuvab valge taustaga graafikaakna pealkirjaga “Liiklusmärk” ja joonistab sinna vabalt valitud
liiklusmärgi (liiklusseaduses määratud liiklusmärke saab vaadata https://www.riigiteataja.ee/akt/103032011006 lisadest).

Mõned innustavad variandid on 112, 175, 178, 438, 712, aga ka siin on soovitatav pigem valida midagi sellist, kus
tsüklid oleksid asjakohased.
"""
from tkinter import *
raam = Tk()
raam.title("Liiklusmärk 111")

# loome tahvli
tahvel = Canvas(raam, width = 552, height = 491)

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()

# algkoordinaadid:
algkoordinaatX = 50
algkoordinaatY = 50

# joonistame kolmnurga küljed:
tahvel.create_polygon((algkoordinaatX, algkoordinaatY + 391, algkoordinaatX + 452, algkoordinaatY + 391, algkoordinaatX + 226, algkoordinaatY + 0), fill = "red", width = 20)
tahvel.create_polygon((algkoordinaatX + 58, algkoordinaatY + 360, algkoordinaatX + 394, algkoordinaatY + 360, algkoordinaatX + 226, algkoordinaatY + 70), fill = "white", width = 20)

#joonistame aia
algkoordinaatX = 141 + algkoordinaatX
algkoordinaatY = 234 + algkoordinaatY
i = 0
while i < 5:
    tahvel.create_rectangle(algkoordinaatX, algkoordinaatY + 19, algkoordinaatX + 34, algkoordinaatY + 34, fill="black", width=0)
    tahvel.create_rectangle(algkoordinaatX, algkoordinaatY + 79, algkoordinaatX + 34, algkoordinaatY + 79 + 15, fill="black", width=0)
    tahvel.create_rectangle(algkoordinaatX + 6, algkoordinaatY + 34, algkoordinaatX + 28, algkoordinaatY + 64 + 45, fill="black", width=0)
    tahvel.create_rectangle(algkoordinaatX, algkoordinaatY + 19, algkoordinaatX + 34, algkoordinaatY + 19 + 15, fill="black", width=0)
    tahvel.create_polygon((algkoordinaatX + 6, algkoordinaatY + 19, algkoordinaatX + 17, algkoordinaatY, algkoordinaatX + 28, algkoordinaatY + 19), fill="black")
    algkoordinaatX = algkoordinaatX + 34
    i += 1

tahvel.create_line(algkoordinaatX + 226, 0, algkoordinaatX + 226, algkoordinaatY + 390, fill="green")
raam.mainloop()
