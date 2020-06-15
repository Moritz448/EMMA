# coding=utf-8

import voice_output

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
            voice_output.voice_output("\nHey! Das ist überhaupt nicht nett!")
            voice_output.voice_output("\nWas willst du mir noch sagen?")
            return True
    return False
