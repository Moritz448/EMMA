# coding=utf-8

insulting_words = [
    "arschloch",
    "blödmann",
    "stinkstiefel",
    "arsch",
    "du schwein",
    "du stinkst",
    "blöde kuh",
    "idiot",
    "petze",
    "blödi",
    "dumme kuh",
    "dumme"
    ]

def is_insulting(sentence):
    words = sentence
    for insulting_word in insulting_words:
        if insulting_word in words:
            print("\nHey! Das ist überhaupt nicht nett!")
            print("\nWas willst du mir noch sagen?")
            return True
    return False
