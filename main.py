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

    talk_ended = False

    while not talk_ended:
        inp = read_sentence()

        answered = False

        if inp == "Tschüß":
            print("Schade, dass du schon gehen willst.",
                  "Bis bald!")
            answered = True
            talk_ended = True

        if not answered:
            answered = reformulate_sentence(inp)

        if not answered:
            answered = ask_after_family(inp)

        if not answered:
            print(random.choice(kommentare), 
                  random.choice(nachfragen))

        print()


