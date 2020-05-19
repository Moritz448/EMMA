# Functon definitions for EMMA

import verbs

# Function for reading and preparing inputs 

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

    return inp


# Function for reformulating the handened sentence

def reformulate_sentence(sentence):

    for i_form, you_form in verbs.i_you_forms:
        beginning = "ich" + i_form + " "

        if sentence.startswith(str(beginning)):
            question = "Warum " + you_form + "Du " + sentence[len(beginning):] + "?"
            print(question)
            return True
        
        return False


