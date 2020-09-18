#Ülesanne 1.4a Nädala ajakulu
"""
Ülikoolides arvestatakse ühe ainepunkti ajakuluks 26 tundi. Näiteks kolme ainepunkti kursusel on ajakuluks 3 * 26 = 78 tundi. Kui see jaotada 10 nädala peale on ühe nädala eeldatav ajakulu 78 / 10 = 7,8.

Koostada programm, mis

küsib kasutajalt just sellises järjekorras ainepunktide arvu (täisarvu) ja nädalate arvu (täisarvu);
arvutab ja väljastab ekraanile ühe nädala eeldatava ajakulu, mis on ümardatud täisarvuni. 
Täisarvuks ümardamisel saab kasutada funktsiooni round, näiteks round(ajakulu) väärtuseks on 8, kui kasutaja on sisestanud 3 ja 10. Funktsioon int ei ole siin sobiv, kuna int(7.8) on hoopis 7. 

Näide programmi tööst:

Sisesta ainepunktide arv:
3
Sisesta nädalate arv:
10
8

"""
print('Sisesta ainepunktide arv:')
ainepunktide_arv = int(input())

print('Sisesta nädalate arv:')
nadalate_arv = int(input())
print(round(ainepunktide_arv * 26 / nadalate_arv ))