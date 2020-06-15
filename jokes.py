# coding=utf-8

import random
import voice_output

# Contains jokes for telling them
jokes = [
    "Was sagt ein Haifisch, wenn er einen Surfer sieht?\n'Das ist aber nett serviert, so mit Frühstücksbrettchen.'",
    "Geht eine schwangere Frau in eine Bäckerei und sagt: 'Ich krieg ein Brot.'\nDarauf der Bäcker: 'Sachen gibt's!'",
    "Geht ein Fahrkartenautomat zum Arzt: 'Herr Doktor, ich krieg die ganze Zeit Geldschein eingesteckt aber spucke nur Münzen aus.\nWas ist nur los mit mir?'\nDoktor: 'Sie sind in den Wechseljahren.'",
    "Was ist braun, knusprig und schwimmt Unterwasser?\nEin Ubrot",
    "Klingelt man beim Metzger, dann sollte man sich nicht wundern, dass kein Schwein aufmacht!",
    "Was liegt auf dem Grund des Ozeans und zittert?\nEin nervöses Wrack",
    "Ich habe heute Morgen meinen Chef gefragt, ob ich auch ein bisschen später zur Arbeit kommen darf.\nEr meinte 'Träum weiter'. Voll nett vom ihm, oder?",
    "Sitzen zwei Hochhäuser auf dem Dachboden und stricken Benzin.\nWas stimmt nicht?\nBenzin darf man nur Häkeln!",
    "Willst du einen Baustellenwitz hören?\nJa\nOk, ich arbeite daran."
]

tell_joke = [
   "erzähl mir einen witz",
   "erzähl mir ein witz",
   "erzähl einen witz",
   "erzähl ein witz",
   "erzähl witz",
   "erzähl nen witz",
   "erzähl mir nen witz",
   "erzähle mir ein witz",
   "erzähle mir einen witz",
   "erzähle einen witz",
   "erzähle ein witz",
   "erzähle witz"
]


def tell_me_joke(sentence):
    for joke_indicator in tell_joke:
        if joke_indicator in sentence:
            voice_output.voice_output("\nOkay\n" + random.choice(jokes))
            return True
        
    return False