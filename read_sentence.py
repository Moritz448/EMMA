# coding=utf-8

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







