# coding=utf-8

import read_sentence

# Contains several variations of "no" in German
no_variations = ["nein",
                 "nö",
                 "ne",
                 "nee",
                 "neee",
                 "neeee",
                 "neeeee",
                 "nope",
                 "niemals",
                 "no"]

# Contains several variations of "yes" in German
yes_variations = ["ja",
                  "jo",
                  "jaa",
                  "jaaa",
                  "jaaaa",
                  "jaaaaa",
                  "yes",
                  "gerne",
                  "yeah",
                  "joa"
]

def i_am_sad(sentence):
    words = sentence.split()
    if "traurig" in words:
        print("\nOh, das tut mir aber leid. Möchtest du mir auch sagen, wieso?")

        answer = read_sentence.read_sentence()
        splitted = answer.split()
        
        for no_word in no_variations:
            if no_word in splitted:
               print("\nSchade.", "Was möchtest du mir noch sagen?") 

        for yes_word in yes_variations:
            if yes_word in splitted:
                print("\nUnd was macht dich traurig?")

        return True
    return False


