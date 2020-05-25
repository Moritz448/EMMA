from functions import reformulate_sentence, i_am_sad, tell_me_poem, is_insulting, reformulate_sentence, ask_after_family, read_sentence
from word_lists import comments, questions

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

            if inp == "tschüss" or inp == "tschüß" or inp == "tschau" or inp == "tschö" or inp == "tschüs" or inp == "bye" or inp == "ciao":
                print("Schade, dass du schon gehen willst. Bis bald!")
                answered = True
                talk_ended = True

            if not answered:
                answered = i_am_sad(inp)

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