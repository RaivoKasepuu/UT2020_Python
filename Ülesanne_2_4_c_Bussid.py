# Kontrollülesanne 2.4c - Bussid
"""
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks.

Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning
väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).

Võib-olla on abi nendest tehetest

// täisarvuline jagamine, 36 // 10 → 3
% jäägi leidmine 36 % 10 → 6
Testige oma programmi muuhulgas järgmiste algandmetega:

inimeste arv: 60, kohtade arv: 40;
inimeste arv: 80, kohtade arv: 40;
inimeste arv: 20, kohtade arv: 40;
inimeste arv: 40, kohtade arv: 40.
Püüdke ka mõista, miks just sellised testandmed valiti.



"""
print("Inimeste arv: ")
inimeste_arv = int(input())
print("Kohtade arv: ")
kohtade_arv = int(input())
busse_vaja = inimeste_arv//kohtade_arv

if inimeste_arv%kohtade_arv == 0:
    print("Busse vaja: " + str(busse_vaja))
    print("viimases bussis inimesi: " + str(kohtade_arv))

else:
    busse_vaja = busse_vaja + 1
    print("Busse vaja: " + str(busse_vaja))
    viimases_bussis = inimeste_arv % kohtade_arv
    print("viimases bussis inimesi: " + str(viimases_bussis))

