from verbs import *
from special_words import *

def form_sentence(sentence):
    

    for i_form, du_form in verbs:
        beginning = "ich " + i_form + " "
        if sentence.startswith(beginning):
            frage = "Warum " + du_form + " Du " + \
                sentence[len(beginning):] + "?"
            print(frage)
            return True
    return False


def nach_familie_fragen(sentence):


    words = sentence.split()
    for family_member in family:
        if family_member in words:
            print("Erzähl mir mehr über deine Familie.")
            return True
    return False


def read_sentence():
    # Text einreadn
    eingabe = input()

    # Leerzeien am beginning und Ende entfernen
    eingabe = eingabe.strip()

    # Mehrere Leerzeien hintereinander
    # durch ein einzelnes ersetzen
    while not eingabe.find("  ") < 0:
        eingabe = eingabe.replace("  ", " ")

    # Punkt am Ende entfernen
    if eingabe.endswith("."):
        eingabe = eingabe[:-1]

    return eingabe
