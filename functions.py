# Functon definitions for EMMA

def read_input():

    # Input text
    inp = input()

    # Remove spaces at the beginning and the end of the input
    inp = inp.strip()

    # Combine several spaces in a row into one
    while not inp.find("  ") < 0:
        inp = inp.replace("  ", " ")

    # Remove the dot at the end
    if inp.endswith("."):
        inp = inp[:-1]

    # Convert everything to lowercase
    inp = inp.lower()
