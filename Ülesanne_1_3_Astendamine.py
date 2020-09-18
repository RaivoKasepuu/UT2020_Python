# Ülesanne 1.3. Astendamine
"""
Koostada programm, mis

küsib kasutajalt astme aluse (täisarv) ja astendaja (täisarv) (just selles järjekorras);
arvutab ja väljastab ekraanile astme.
Näiteks kui kasutaja sisestab vastustena 2 ja 4, siis väljastatakse 16, sest 24 = 16. Astme alus on siin 2, astendaja 4 ja aste 16.

Näide programmi tööst:
Sisesta astme alus:
4
Sisesta astendaja:
2
16


"""

print('Sisesta astme alus: ')
astme_alus = int(input())

print('Sisesta astendaja: ')
astendaja = int(input())
print(astme_alus ** astendaja)

