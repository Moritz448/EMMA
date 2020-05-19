from verbs import *
from special_words import *

def satz_umformulieren(satz):
    

    for ich_form, du_form in verben:
        anfang = "Ich " + ich_form + " "
        if satz.startswith(anfang):
            frage = "Warum " + du_form + " Du " + \
                satz[len(anfang):] + "?"
            print(frage)
            return True
    return False


def nach_familie_fragen(satz):


    woerter = satz.split()
    for familienmitglied in familienmitglieder:
        if familienmitglied in woerter:
            print("Erzähl mir mehr über deine Familie.")
            return True
    return False


def lese_satz():
    # Text einlesen
    eingabe = input()

    # Leerzeichen am Anfang und Ende entfernen
    eingabe = eingabe.strip()

    # Mehrere Leerzeichen hintereinander
    # durch ein einzelnes ersetzen
    while not eingabe.find("  ") < 0:
        eingabe = eingabe.replace("  ", " ")

    # Punkt am Ende entfernen
    if eingabe.endswith("."):
        eingabe = eingabe[:-1]

    return eingabe
