from functions import *

import random


def lili():
    kommentare = ["Das klingt interessant.", "Aha."]
    nachfragen = ["Erzähl mir mehr davon!",
                  "Woruber willst du noch sprechen?",
                  "Und weiter?"]

    print("Hallo! Mein Name ist LILI. Schön, dass du",
          "mit mir sprechen willst. Wenn du keine Lust",
          "mehr hast, sag einfach 'Tschüß'.",
          "Was möchtest du mir heute erzählen?")
    print()

    gespraech_zu_ende = False

    while not gespraech_zu_ende:
        eingabe = lese_satz()

        geantwortet = False

        if eingabe == "Tschüß":
            print("Schade, dass du schon gehen willst.",
                  "Bis bald!")
            geantwortet = True
            gespraech_zu_ende = True

        if not geantwortet:
            geantwortet = satz_umformulieren(eingabe)

        if not geantwortet:
            geantwortet = nach_familie_fragen(eingabe)

        if not geantwortet:
            print(random.choice(kommentare), 
                  random.choice(nachfragen))

        print()


