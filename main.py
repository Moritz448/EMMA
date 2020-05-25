# coding=utf-8

from functions import *
from word_lists import comments, questions, goodbye

import random


def emma():

    try:

        print("\n##############################################################\nHallo! Mein Name ist EMMA. Schön, dass du",
              "mit mir\nsprechen willst. Wenn du keine Lust",
              "mehr hast, sag\neinfach 'Tschüss'.",
              "Was möchtest du mir heute erzählen?",
              "\n##############################################################\n")


        talk_ended = False

        while not talk_ended:
            inp = read_sentence()

            answered = False

            for bye_word in goodbye:
                if inp == bye_word: 
                    print("Schade, dass du schon gehen willst. Bis bald!")
                    answered = True
                    talk_ended = True

            if not answered:
                answered = i_am_sad(inp)

            if not answered:
                answered = tell_me_joke(inp)

            if not answered:
                answered = calculate(inp) 

            if not answered:
                answered = tell_me_poem(inp)

            if not answered:
                answered = is_insulting(inp)

            if not answered:
                answered = reformulate_sentence(inp)

            if not answered:
                answered = ask_after_family(inp)

            if not answered:
                print(random.choice(comments), 
                      random.choice(questions))

            print()
    except KeyboardInterrupt:
        print("Schade, dass du schon gehen willst. Bis bald!")


emma()