# coding=utf-8

import random
import voice_output
# Contains Poems for telling them
poems  = [
    ("\nSpinoza\nHier liegt ein Eichbaum umgerissen,\nSein Wipfel tät die Wolken küssen,\nEr liegt am Grund – warum?\nDie Bauren hatten, hör ich reden,\nSein schönes Holz zum Baun vonnöten\nUnd rissen ihn deswegen um.\nJohann Christoph Friedrich Schiller"),
    ("\nWeisheit und Klugheit\nWillst du, Freund, die erhabensten Höhn der Weisheit erfliegen,\nWag es auf die Gefahr, daß dich die Klugheit verlacht.\nDie kurzsichtige sieht nur das Ufer, das dir zurückflieht,\nJenes nicht, wo dereinst landet dein mutiger Flug.\nJohann Christoph Friedrich Schiller"),
    ("\nTugend des Weibes\nTugenden brauchet der Mann, er stützet sich wagend ins Leben,\nTritt mit dem stärkeren Glück in den bedenklichen Kampf.\nEine Tugend genüget dem Weib, sie ist da, sie erscheinet,\nLieblich dem Herzen, dem Aug lieblich erscheine sie stets.\nJohann Christoph Friedrich Schiller"),
    ("\nSäume nicht, dich zu erdreisten,\nwenn die Menge zaudernd schweift;\nAlles kann der Edle leisten,\nder versteht und rasch ergreift.\nJohann Wolfgang von Goethe"),
    ("\nDem schlechtsten Ding an Art und an Gehalt\nleiht Liebe dennoch Ansehn und Gehalt.\nSie sieht mit dem Gemüt, nicht mit den Augen,\nund ihr Gemüt kann nie zum Urteil taugen\nWilliam Shakespeare"),
    ("\nEinsam wandle deine Bahnen,\nstilles Herz, und unverzagt;\nviel erkennen, vieles ahnen\nwirst du, was dir keiner sagt.\nJoseph Viktor von Scheffel"),
    ("\nHerze, willst du ganz genesen,\nsei selber wahr, sei selber rein!\nWas wir in Welt und Menschen lesen,\nist nur der eigne Widerschein.\nTheodor Fontane")
]

tell_poem = [
   "erzähl mir ein gedicht",
   "erzähl ein gedicht",
   "erzähle mir ein gedicht",
   "erzähle ein gedicht",
   "ich will ein gedicht",
   "ich will ein gedicht hören",
   "ich möchte ein gedicht" 
]


def tell_me_poem(sentence):
    for poem_indicator in tell_poem:
        if poem_indicator in sentence:
            voice_output.voice_output("\nOkay\n" + random.choice(poems))
            return True
        
    return False
