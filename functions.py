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
    # Text einreadn
    inp = input()

    # Leerzeien am beginning und Ende entfernen
    inp = inp.strip()

    # Mehrere Leerzeien hintereinander
    # durch ein einzelnes ersetzen
    while not inp.find("  ") < 0:
        inp = inp.replace("  ", " ")

    # Punkt am Ende entfernen
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
