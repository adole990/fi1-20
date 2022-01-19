import random


a = random.randint(1, 100)
b = random.randint(1, 100)
c = a * b
versuche = 0
while True:
    eingabe = int(input(f"Aufgabe: {a} * {b} = "))
    if eingabe == c:
        print(f"Richtig. Anzahl versuche {versuche + 1}")
        break
    elif c - 2 <= eingabe <= c + 2:
        versuche += 1
        print(f"Nahe dran. Anzahl Versuche: {versuche}")

    else:
        versuche += 1
        print(f"Weit weg. Anzahl Versuche: {versuche}")
