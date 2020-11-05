def TeineSuurem(int1, int2):
    if int1 > int2:
        return True
    else:
        return False


lahkunud = []
saabunud = []

file = open("lahkunud.txt", encoding="UTF-8")
for row in file:
    lahkunud.append(row)
file.close()
print("järjend lahkunud")
print(lahkunud)
print()
file = open("saabunud.txt", encoding="UTF-8")
for row in file:
    saabunud.append(row)
file.close()
print("järjend saabunud")
print(saabunud)

print()

print("leiame mõlema järjendi esimese elemendi ja castime selle integeriks:")
print(int(lahkunud[0].split(" ")[1]))
print(int(saabunud[0].split(" ")[1]))


print(len(lahkunud))
print(len(saabunud))
välja = []
sisse = []

for i in range(len(lahkunud)):
    välja.append(int(str(lahkunud[i].split(" ")[1])))

for i in range(len(saabunud)):
    sisse.append(int(str(saabunud[i].split(" ")[1])))

print(sisse)
print(välja)


print("Mitmel aastal oli sisseränne suurem, kui väljaränne: ")

counter = 0

for i in range(len(sisse)):
    if TeineSuurem(sisse[i], välja[i]):
        counter += 1

print(counter)


print("Milisel aastal oli erinevus suurim?")

aasta = 2000
max = 0
maxAasta = 2000

for i in range(len(sisse)):
    vahe = sisse[i] - välja[i]
    if vahe > max:
        max = vahe
        print(max, aasta)
        maxAasta = aasta
    aasta += 1

print(maxAasta)
print(max)


print("Mitmel aastal on ränne kasvanud?")

counter = 0

for i in range(len(sisse)):
    vahe = sisse[i] - välja[i]
    if TeineSuurem(sisse[i], välja[i]):
        counter += 1


print(counter)
