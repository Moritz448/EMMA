# coding=utf-8

import random

import verbs
import forbidden_words
import family
import jokes
import calculate
import poems
import read_sentence
import sad
import word_lists


def emma():

    try:

        print("\n##############################################################\nHallo! Mein Name ist EMMA. Schön, dass du",
              "mit mir\nsprechen willst. Wenn du keine Lust",
              "mehr hast, sag\neinfach 'Tschüss'.",
              "Was möchtest du mir heute erzählen?",
              "\n##############################################################\n")
        
        print("""                                                                                                                      
                                                                                                                       
                                                                                                                       
                   ,,,,,,,,,.                                                                                          
             ,///******                                                                                                
           //////*.   ***********                                                                                      
        .///////  .///***************                                                                                  
       *//////, ./////,       .,*******                .........    ...      ...      ...      ...         ..          
      *(/////  ,///,  .////***,  .******.              ,,,          ,,,,    .,,,,    .,,,,     ,,,,      .,,,,.        
      ((((//* .///.  ////,  //**  ,******              ,,,         .,,,,,   ,, ,,    .,,,,,  .,,,,,      ,,,.,,        
      ((((((  .///  ./////,  ///*  ******,             ,,,,,,,,    .,,.,,, ,,, ,,    .,, ,,, ,,.,,,     ,,.  ,,,       
      (((((((  ////   ///.  ,///  ,******              ,,,         .,,  .,,,,  ,,,   ,,,  ,,,,.  ,,    ,,,,,,,,,,      
       ((((((,  *(////...*/////. .///***.              ,,,         ,,,   ,,,   ,,,   ,,,   ,,,   ,,,  .,,      ,,,     
       ,(((((((,  ./////////,  .///////,               .,,,,,,,,   ,,,         .,,   ,,.         ,,,  ,,.       ,,     
         (((((((((*.        ,/////////.                                                                                
           ,(((((((((((((///////////.                                                                                  
              .(((((((((((((////*                                                                                      
                       /                                                                                               
                                                                                                                       
                                                                                                                       
                                                                                                                       """)


        talk_ended = False

        while not talk_ended:
            finished_inp = read_sentence.read_sentence()

            answered = False

            for bye_word in word_lists.goodbye:
                if finished_inp == bye_word: 
                    print("Schade, dass du schon gehen willst. Bis bald!")
                    answered = True
                    talk_ended = True

            if not answered:
                if finished_inp == "":
                    finished_inp = read_sentence.read_sentence()
                    answered = True

            if not answered:
                answered = sad.i_am_sad(finished_inp)

            if not answered:
                answered = jokes.tell_me_joke(finished_inp)

            if not answered:
                answered = calculate.calculate(finished_inp) 

            if not answered:
                answered = poems.tell_me_poem(finished_inp)

            if not answered:
                answered = forbidden_words.is_insulting(finished_inp)

            if not answered:
                answered = verbs.reformulate_sentence(finished_inp)

            if not answered:
                answered = family.ask_after_family(finished_inp)

            if not answered:
                print(random.choice(word_lists.comments), 
                      random.choice(word_lists.questions))


            print()
    except KeyboardInterrupt:
        print("Schade, dass du schon gehen willst. Bis bald!")


emma()