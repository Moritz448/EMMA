# coding=utf-8

import speech_recognition as sr
import sys

def read_sentence():


    global inp

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        inp = r.recognize_google(audio, language="de_DE")

    except sr.UnknownValueError:
        print("Fehler bei der Spracherkennung!! Bitte versuche es erneut!!\n")
        inp = ""

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



