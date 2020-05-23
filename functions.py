from verbs import *
from special_words import *

def reformulate_sentence(sentence):
    

    for i_form, you_form in verbs:
        beginning = "ich " + i_form + " "
        if sentence.startswith(beginning):
            frage = "Warum " + you_form + " Du " + \
                sentence[len(beginning):] + "?"
            print(frage)
            return True
    return False


def ask_after_family(sentence):
    
    words = sentence.split()
    for family_member in family:
        if family_member in words:
            print("Erzähl mir mehr über deine Familie.")
            return True
    return False


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

def i_am_sad(sentence):
    words = sentence.split()
    if "traurig" in words:
        print("Oh, das tut mir aber leid. Möchtest du mir auch sagen, wieso?")
        return True
    return False
