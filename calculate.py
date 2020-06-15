# coding=utf-8

import voice_output

calculate_words  =[
   "mir ist langweilig",
   "langweilig",
   "ich möchte rechnen",
   "ich möchte rechnen üben",
   "ich will rechnen"
]

def calculate(sentence):
    def make_calc_task():

        voice_output.voice_output("Okay. Hier kommt eine Rechenaufgabe:\n")
        def check_answer():


            answer = input("\nWas ergibt 5 + 5?\n")

            if int(answer) == 10:
                voice_output.voice_output("Das ist Richtig!!")
                return True

            else:
                voice_output.voice_output("\nDas ist leider falsch!")
                check_answer()

        check_answer()


    for calc_indicator in calculate_words:
        if calc_indicator in sentence:
            make_calc_task()
            return True
    
    return False