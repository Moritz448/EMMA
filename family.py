# coding=utf-8


family = [ 

    # a few different words for "mother" in German
    "mutter",
    "mutti",
    "mama",
    "mami",
    "mum",
    "mammi",
    "mamma",
    "mummy",
    "stiefmama",
    "stiefmami",
    "stiefmutter",
    
    # a few different words for "father" in German 
    "vater",
    "vati",
    "papa",
    "papi",
    "dad",
    "daddy",
    "paps",
    "stiefpapa",
    "stiefpapi",
    "stiefvater",


    # a few different words for "brother" in German
    "bruder",
    "brüderchen",
    "bruderherz",

    # a few different words for "sister" in German
    "schwester",
    "schwesterchen",
    "schwesterherz",

    # Words for "grandfather" and "grandmother" in German
    "opa",
    "oma",
    "opi",
    "omi",
    "großvater",
    "großmutter",
    "großpapa",
    "großmama",
    "großpapi",
    "großmami",

    # Another family words in German
    "zwilling",
    "zwillinge",

    "drilling",
    "drillinge",
    
    "vierling",
    "vierlinge",
]

def ask_after_family(sentence):
    words = sentence.split()
    for family_member in family:
        if family_member in words:
            print("\nErzähl mir mehr über deine Familie.")
            return True
    return False
