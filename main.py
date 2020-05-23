from functions import *
from word_lists import *

import random


def emma():

    print("Hallo! Mein Name ist EMMA. Schön, dass du",
          "mit mir sprechen willst. Wenn du keine Lust",
          "mehr hast, sag einfach 'Tschüss'.",
          "Was möchtest du mir heute erzählen?")
    print()

    talk_ended = False

    while not talk_ended:
        inp = read_sentence()

        answered = False

        if inp == "tschüss" or inp == "tschüß":
            print("Schade, dass du schon gehen willst. Bis bald!")
            answered = True
            talk_ended = True

        if not answered:
            answered = reformulate_sentence(inp)

        if not answered:
            answered = ask_after_family(inp)

        if not answered:
            print(random.choice(comments), 
                  random.choice(questions))

        print()


emma()