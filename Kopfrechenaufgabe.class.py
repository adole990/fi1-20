import random
from threading import Timer
import csv


class SpielAufgabe:
    erste_zahl = random.randint(1, 100)
    zweite_zahl = random.randint(1, 100)

    """def __init__(self, spieler_name):
        self.spieler_name = spieler_name
        self.spieler_gewinn_punkte = 0"""

    def gib_summe(self):
        return self.erste_zahl + self.zweite_zahl

    def spiel_start(self):
        summe = self.gib_summe()
        versuche = 0
        zeit_abgelaufen_msg = """
 ,--.  
| oo | 
| ~~ | Zeit ist abgelaufen:  o  o  o 
|/\/\| 
-------------------------------------------------------------------------
"""
        zeit_ist_um_in_sek = 20  #Zeit für die Eingabe
        zeitt = Timer(zeit_ist_um_in_sek, print, [zeit_abgelaufen_msg])
        zeitt.start()
        spieler_name = input("Bitte Name eingeben : ")
        while True:
            benutzer_eingabe_zahl = int(input(f"Aufgabe: {self.erste_zahl} + {self.zweite_zahl} = "))
            if benutzer_eingabe_zahl == summe:
                print("-------------------------------------------------------------------------")
                print(
                    f"-> Bingo! du hast gewonnen. Anzahl Versuche: {versuche + 1}")
                print("-------------------------------------------------------------------------")
                #name = input("Name eingeben : ")
                doom = [spieler_name, versuche]
                with open('test.csv', 'r') as infile:
                    reader = list(csv.reader(infile))
                    reader.insert(1, doom)
                with open('test.csv', 'w') as outfile:
                    writer = csv.writer(outfile)
                    for line in reader:
                        writer.writerow(line)
                break
            elif benutzer_eingabe_zahl != summe:
                print("Falsch!, versuche nochmal:")
                versuche += 1

                    #writer.writerow(["Name", "Anzahl Versuche"])
                    #writer.writerow(["Heisenberg", "Banana Banana Banana"])

        zeitt.cancel()


aaaa = SpielAufgabe()
aaaa.spiel_start()
