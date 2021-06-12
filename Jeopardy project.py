import random
import os
from utilities import answers_read,code_read,vocab_read,syntax_read, clear_screen,instructions,random_players,fun_Facts 

def add_score(name,score):
    for k, v in players_stats.items():
        if name == k:
            v += score
            players_stats[k] = v
def subtract_score(name,score):
    for k, v in players_stats.items():
        if name == k:
            v -= score
            players_stats[k] = v

players_stats = {"Jason": 0, "Brad Rutter": 0, "Ken Jennings": 0}

def main():
    print(
    """
          (_)                              | |      
           _  ___  ___  _ __   __ _ _ __ __| |_   _ 
          | |/ _ \/ _ \| '_ \ / _` | '__/ _` | | | |
          | |  __/ (_) | |_) | (_| | | | (_| | |_| |
          | |\___|\___/| .__/ \__,_|_|  \__,_|\__, |
         _/ |          | |                     __/ |
        |__/           |_|                    |___/
                                                      
    ===================================================
    """
    )
    
    selection = 0
    max = 0
    
    menu = ("1.) Start Game","2.) Exit") 
    
    players_name = ["Jason","Brad Rutter","Ken Jennings"]
    player = ""
    raw_input = ("\nPress <ENTER> to continue...")
    guess = (" ")
       
    used_questions = []
    questions_answered = 0
    MAX_QUESTIONS = 15
    
    answers = answers_read()
    code = code_read()
    vocab = vocab_read()
    syntax = syntax_read()
    funFacts = fun_Facts()
    "========================================================"

    clear_screen()

    while selection != 2:
        print(menu[0])
        print(menu[1])

        instructions()

        selection = int(input("Please select an option: "))
        
        input(raw_input)
        "======================================================"

        clear_screen()
        
        if selection == 1:
            print("Todays players are",players_name[0],",",players_name[1],",",players_name[2],"\n")
            print("Todays cateorgies are... code, vocabulary, and syntax")
            
            while questions_answered != MAX_QUESTIONS:
                
                selected_player = random_players(players_name)
                print("Player selected is", selected_player)
                try:
                    player_choice = input("\nplease choose a category(code,vocabulary,syntax): ").lower()
                    if player_choice == "code":
                        if len(code) == 0:
                            raise ValueError("That list is empty please choose other list.")
                            player_choice == False
                    if player_choice == "vocabulary":
                        if len(vocab) == 0:
                            raise ValueError("That list is empty please choose other list.")
                    if player_choice == "syntax":
                        if len(syntax) == 0:
                            raise ValueError("That list is empty please choose other list.")
                except ValueError:
                    print("That list is empty please choose other list.")
                    
                else:
                    flag = 0
                    try:
                        points = int(input("\nEnter point amount you wish to guess (200,400,600,1000): "))
                        
                    except ValueError:
                        print("You did not enter a number!")
                        
                    else:
                        if points != 200 and points != 400 and points != 600 and points != 1000:
                            print("Incorrect value")
                            guess = False
                        
                        if player_choice != 'code' and player_choice != 'vocabulary' and player_choice != 'syntax':
                            guess = False
                            
                        if guess == False:
                                print("You did not pick a category.")
                             
                        elif player_choice == 'code':
                            question = random.choice(code)
                            print("\n",question)
                            code.remove(question)
                            guess = input("\nWhat is: ").lower()
                        
                        elif player_choice == 'vocabulary':
                            question = random.choice(vocab)
                            print("\n",question)
                            vocab.remove(question)
                            guess = input("\nWhat is: ").lower()

                        elif player_choice == 'syntax':
                            question = random.choice(syntax)
                            print("\n",question)
                            syntax.remove(question)
                            guess = input("What is: ").lower()
                        
                        with open("answers.txt") as answers:
                            list_answers = answers.readlines()
                            for a in range(len(list_answers)):
                                if guess == list_answers[a][:-1]:
                                    flag = 1
                                    print("Correct!")
                                    add_score(selected_player,points)
                                    questions_answered += 1
                                
                            if flag == 0:
                                print("Incorrect!")
                                questions_answered += 1
                                subtract_score(selected_player,points)
                                
                        trivia = random.choice(funFacts)
                        print("\n",trivia)      
                        input(raw_input)
                        clear_screen()

            for k, v in players_stats.items():
                print(k,v)
                if max < v:
                    max = v
                    player = k

            print("The winner is",player)
                   
        if selection == 2:
            print("exiting program")
                           
              
main()
