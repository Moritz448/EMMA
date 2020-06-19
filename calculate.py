# coding=utf-8

import random

calculate_words  = [
   "mir ist langweilig",
   "langweilig",
   "ich möchte rechnen",
   "ich möchte rechnen üben",
   "ich will rechnen"
]


def if_calculate_word(sentence):
    for calc_indicator in calculate_words:
        if calc_indicator in sentence:
            make_calc_task(choose_operand(), choose_operator(), choose_operand())
            return True
    
    return False


    


def choose_operator():
    op = random.randint(1, 5)
    
    if op == 1:
        return "plus"

    if op == 2:
        return "minus"

    if op == 3:
        return "multiplicate"

    if op == 4:
        return "divide"

def choose_operand():
    operand = random.randint(0, 1000)
    return operand 

def make_calc_task(op1, operator, op2):

    global task_solution


    if operator == "plus":

        def plus():
            task_solution = op1 + op2
            print("Und hier kommt die Aufgabe: ")
            x = input("Was ergibt", op1, "+", op2, "??")
            if x == task_solution:
                print("Richtig!!!!")
                return True
            else:
                print("Leider falsch! Versuche es erneut:")
                plus()
    
        def minus():
            task_solution = op1 - op2
            print("Und hier kommt die Aufgabe: ")
            x = input("Was ergibt", op1, "-", op2, "??")
            if x == task_solution:
                print("Richtig!!!!")
                return True
            else:
                print("Leider falsch! Versuche es erneut:")
                minus()

        def multiplicate():
            task_solution = op1 * op2
            print("Und hier kommt die Aufgabe: ")
            x = input("Was ergibt", op1, "*", op2, "??")
            if x == task_solution:
                print("Richtig!!!!")
                return True
            else:
                print("Leider falsch! Versuche es erneut:")
                multiplicate()

        def divide():
            task_solution = op1 / op2
            print("Und hier kommt die Aufgabe: ")
            x = input("Was ergibt", op1, "+", op2, "??")
            if x == task_solution:
                print("Richtig!!!!")
                return True
            else:
                print("Leider falsch! Versuche es erneut:")
                divide()