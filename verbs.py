# coding=utf-8

verbs = [ 
        ("mag", "magst"),
        ("liebe", "liebst"),
        ("spiele", "spielst"),
        ("habe", "hast"),
        ("gehe", "gehst"),
        ("rede", "redest"),
        ("laufe", "läufst"),
        ("spreche", "sprichst"),
        ("renne", "rennst"),
        ("bin", "bist"),
        ("kriege", "kriegst"),
        ("will", "willst"),
        ("möchte", "möchtest")
        ]

def reformulate_sentence(sentence):
    
    for i_form, you_form in verbs:
        beginning = "ich " + i_form + " "
        if sentence.startswith(beginning):
            frage = "Warum " + you_form + " Du " + \
                sentence[len(beginning):] + "?"
            print("\n", frage)
            return True
    return False