# coding=utf-8

import random

import verbs
import forbidden_words
import family
import jokes
import calculate
import poems
import read_sentence
import sad
import word_lists


def emma():

    try:

        print("\n##############################################################\nHallo! Mein Name ist EMMA. Schön, dass du",
              "mit mir\nsprechen willst. Wenn du keine Lust",
              "mehr hast, sag\neinfach 'Tschüss'.",
              "Was möchtest du mir heute erzählen?",
              "\n##############################################################\n")


        talk_ended = False

        while not talk_ended:
            inp = read_sentence.read_sentence()

            answered = False

            for bye_word in word_lists.goodbye:
                if inp == bye_word: 
                    print("Schade, dass du schon gehen willst. Bis bald!")
                    answered = True
                    talk_ended = True

            if not answered:
                answered = sad.i_am_sad(inp)

            if not answered:
                answered = jokes.tell_me_joke(inp)

            if not answered:
                answered = calculate.calculate(inp) 

            if not answered:
                answered = poems.tell_me_poem(inp)

            if not answered:
                answered = forbidden_words.is_insulting(inp)

            if not answered:
                answered = verbs.reformulate_sentence(inp)

            if not answered:
                answered = family.ask_after_family(inp)

            if not answered:
                print(random.choice(word_lists.comments), 
                      random.choice(word_lists.questions))

            print()
    except KeyboardInterrupt:
        print("Schade, dass du schon gehen willst. Bis bald!")


emma()