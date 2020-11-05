from random import randint


"""
Täringu emuleerimine

"""
# Täringute külgede arvu küsimine koos kontrolliga:
while True:
    try:
        sides = int(input("sisestage täringu külgede arv (paarisarv lõigul 6...10): "))
        if sides == 6 or sides == 8 or sides == 10:
            break
        else:
            print("järgigem ikka reegleid..")
    except ValueError:
        print("Viga! Lubamatu sümbol! Sisestage uuesti!")

print(sides)

# Täringute visete arvu küsimine koos kontrolliga:
while True:
    try:
        diceCount = int(input("sisestage visete arv 2...5): "))
        if 2 <= diceCount <= 5:
            break
        else:
            print("järgigem ikka reegleid..")
    except ValueError:
        print("Viga! Lubamatu sümbol! Sisestage uuesti!")

print(diceCount)


print("*******************")
total = 0
dices = []
while diceCount > 0:

    dice = randint(1, sides)

    # dice = 5 # alati üks tulemus visetel - add-i testimiseks
    dices.append(dice)
    print(dice)

    total += dice
    diceCount -= 1

add = (sides + dice - 2) ** 2
for i in range(1, len(dices)):
    if dices[i] != dices[i - 1]:
        add = 0

print("*******************")
print(total + add)

