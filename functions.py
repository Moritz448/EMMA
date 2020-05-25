# coding=utf-8

from verbs import verbs
from special_words import family, tell_poem, tell_joke
from word_lists import no_variations, yes_variations
from forbidden_words import insulting_words
import random
from poems import poems
from jokes import jokes


def read_sentence():

    # Input text
    inp = input()

    # Delete Whitespaces at the beginning and the end
    inp = inp.strip()

    # Merge many Whitespaces to one
    while not inp.find("  ") < 0:
        inp = inp.replace("  ", " ")

    # Delete the dot at the end
    if inp.endswith("."):
        inp = inp[:-1]

    inp = inp.lower()

    return inp


def reformulate_sentence(sentence):
    

    for i_form, you_form in verbs:
        beginning = "ich " + i_form + " "
        if sentence.startswith(beginning):
            frage = "Warum " + you_form + " Du " + \
                sentence[len(beginning):] + "?"
            print("\n", frage)
            return True
    return False


def ask_after_family(sentence):

    words = sentence.split()
    for family_member in family:
        if family_member in words:
            print("\nErzähl mir mehr über deine Familie.")
            return True
    return False


def i_am_sad(sentence):
    words = sentence.split()
    if "traurig" in words:
        print("\nOh, das tut mir aber leid. Möchtest du mir auch sagen, wieso?")

        answer = read_sentence()
        splitted = answer.split()
        
        for no_word in no_variations:
            if no_word in splitted:
               print("\nSchade.", "Was möchtest du mir noch sagen?") 

        for yes_word in yes_variations:
            if yes_word in splitted:
                print("\nUnd was macht dich traurig?")

        return True
    return False


def is_insulting(sentence):

    words = sentence
    
    for insulting_word in insulting_words:
        if insulting_word in words:
            print("\nHey! Das ist überhaupt nicht nett!")
            print("\nWas willst du mir noch sagen?")
            return True
    return False


def tell_me_poem(sentence):
    for poem_indicator in tell_poem:
        if poem_indicator in sentence:
            print("\nOkay" + "\n" + random.choice(poems))
            return True
        
        return False


def tell_me_joke(sentence):
    for joke_indicator in tell_joke:
        if joke_indicator in sentence:
            print("\nOkay" + "\n" + random.choice(jokes))
            return True
        
        return False
