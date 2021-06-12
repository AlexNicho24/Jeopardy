#-------------------------------------------------------------------------------
# IT Jeopardy Game show 
# Student Names: Alex Nicholas
# Assignment: Final Project main file
# Submission Date: 12/08/2017
# Python Version: 3.6.0
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Jeopardy ASCII ART
#-------------------------------------------------------------------------------
# Note: (a note to the grader as to any problems or uncompleted aspects of
# of the assignment)
#-------------------------------------------------------------------------------
# Pseudocode:
# import random, os and functions in utilities files
# define function that adds score of player and subtracts score of player
# create dict of players_stats
# define main function
# PRINT title of Game show
# initialize variables: selection,max,raw_input,guess,player,menu,player_name
# questions_answered, max_questions
# assign functions to variables
# while selection does not equal 2
#   PRINT menu
#   instructions function printed
#   INPUT user selection
#   INPUT raw_input
#   program clears screen
#   IF selection does equal 1
#       print player names
#       print categories of jeopardy game
#       while questions_answered does not equal MAX_Questions
#           player is randomly selected and assigned to selected_player
#           PRINT the selected player
#           try
#               user inputs a category between code
#               IF player choice equals code
#                   IF code is checked and empty
#                       raise an ValueError and PRINT list is empty
#           except valueError
#               PRINT list empty please choose
#           else
#               flag is initialized and equals 0
#               error is initialized and equals 0
#               try
#                   user inputs the amount of points they want
#               except valueError
#                   IF user does not enter an int PRINT please enter a score!
#               else
#                   IF points does not equal 200,400,600,and 1000
#                       points is equal to False
#                       error equals 1
#                   IF player choice does not equal code, vocabulary, and syntax
#                       guess is equal to False
#                       error equals 1
#                   IF points equals False
#                       PRINT Incorrect value
#                   ELIF guess equals False
#                       PRINT you did not pick a category
#                   ELIF player_choice equals code
#                       random list number from the file "code" is assigned to question
#                       PRINT question
#                       remove list number from code
#                       guess equals user input
#                   ELIF player_choice equals vocabulary
#                       random list number from the file "vocab" is assigned to question
#                       PRINT question
#                       remove list number from vocab
#                       guess equals user input
#                   ELIF player_choice equals syntax
#                       random list number from the file "syntax" is assigned to question
#                       PRINT question
#                       remove list number from syntax
#                       guess equals user input
#                   IF error equals 1
#                       PRINT restarting game...
#                   ELSE
#                       program opens the file answers as answers
#                       list_answers is created and equals answers as a list
#                       FOR a in range of the number of elements in list_answers
#                           IF guess equals an element in list_answers
#                               flag equals 1
#                               PRINT Correct!
#                               add_scores function passes the selected_player and the points
#                               questions_answered is added by 1
#                       IF flag equals 0
#                           PRINT Incorrect!
#                           questions_answered is added by 1
#                           subtract_score passes the selected_player and points
#                   trivia equals random selected element from funFacts file
#                   PRINT trivia
#                   INPUT raw_input
#                   clear_screen
#             FOR k and v in player_stats items
#               print k and v
#               IF max is less than v
#                   max equals v
#                   player equals k
#             PRINT The winner is ,player
#    IF selection equals 2
#       player choice equals user input of category
#       IF player_choice equals code,vocabulary or syntax
#           file is opened
#           user is asked to input the new question
#           new question is added to file
#           file is closed
#           max questions is added by 1
#       IF player_choice equals none of categories
#           PRINT error adding questions restarting program
#    IF selection equals 3
#       PRINT exiting program
#close main function
#-------------------------------------------------------------------------------
# Source Code:

#imports random, os, and utilities file that contains most of the functions
import random
import os
from utilities import answers_read,code_read,vocab_read,syntax_read, clear_screen,instructions,random_players,fun_Facts 

def add_score(name,score):
    """
    input: name, score
    Description:If the user gets the answer right this function
    adds the amount the player asked to their total score 
    """
    for k, v in players_stats.items():
        if name == k:
            v += score
            players_stats[k] = v
            
def subtract_score(name,score):
    """
    input: name, score
    Description: If the user gets the answer wrong this function
    subtracts the amount the player asked from their total score
    """
    for k, v in players_stats.items():
        if name == k:
            v -= score
            players_stats[k] = v
            
#dict of players scores
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
    #intializing variables 
    selection = 0
    max = 0
    #holds the game until user input
    raw_input = ("\nPress <ENTER> to continue...")
    #intializes empty string 
    guess = ""
    #displays winner
    player = ""

    #Creates menu for player to choose
    menu = ("1.) Start Game","2.) Add question","3.) Exit") 

    #List of players to be called later in-game
    players_name = ["Jason","Brad Rutter","Ken Jennings"]
    
    #Tallys questions answered until max
    questions_answered = 0
    max_questions = 15
    
    #assigns functions to a variable
    answers = answers_read()
    code = code_read()
    vocab = vocab_read()
    syntax = syntax_read()
    funFacts = fun_Facts()
    "========================================================"
    
    #Loops game until user wants to quit
    while selection != 3:
        #Instructions on how to play the game
        instructions()

        print(menu[0])
        print(menu[1])
        print(menu[2])
        
        #User input to start game or end it
        selection = int(input("Please select an option: "))

        #enter to continue
        input(raw_input)
        
        "======================================================"
        #clear cmd
        clear_screen()

        #Starts game
        if selection == 1:
            print("Todays players are",players_name[0],",",players_name[1],",",players_name[2],"\n")
            print("Todays cateorgies are... code, vocabulary, and syntax")
            
            #core of game repeats until max questions
            while questions_answered != max_questions:
                #randomly selected player
                selected_player = random_players(players_name)
                print("Player selected is", selected_player)
                #if category is empty raises an error asking user to enter a different category
                try:
                    player_choice = input("\nplease choose a category(code,vocabulary,syntax): ").lower()
                    
                    if player_choice == "code": #user input equals string
                        if len(code) == 0: #checks if list empty
                            raise ValueError("That category is empty please choose other.") 
                            
                    if player_choice == "vocabulary": #user input equals string
                        if len(vocab) == 0: #checks if list empty
                            raise ValueError("That category is empty please choose other.")
                        
                    if player_choice == "syntax": #user input equals string
                        if len(syntax) == 0: #checks if list empty
                            raise ValueError("That category is empty please choose other.")
                except ValueError:
                    print("That category is empty please choose other.") #pulls string from except to raise valueError
   
                else:
                    flag = 0 #intializes variable
                    error = 0 #intializes variable
                    try:
                        #displays scores to pick from
                        points = int(input("\nEnter point amount you wish to guess (200,400,600,1000): "))
                        
                    except ValueError: #raises error if user input is not a number
                        print("You did not enter a number!")
                        
                    else:
                        #checks if user input != selected integers
                        if points != 200 and points != 400 and points != 600 and points != 1000:
                            #assigns points to false
                            points = False
                            error = 1 #adds 1 to error
                        #Checks if user input != to categories 
                        if player_choice != 'code' and player_choice != 'vocabulary' and player_choice != 'syntax':
                            #assigns guess to false
                            guess = False
                            error = 1 #adds 1 to error
                          
                        if points == False: #catches error nad notifies user
                            print("Incorrect value")    
                        elif guess == False: #catches error nad notifies user
                            print("You did not pick a category.")
                             
                        elif player_choice == 'code': #user_input == "code"
                            question = random.choice(code)#randomly selects a question out of 5 from the file
                            print("\n",question) #prints question
                            code.remove(question) #removes question from list
                            guess = input("\nWhat is: ").lower() #user guesses answer
                        
                        elif player_choice == 'vocabulary': #user_input == "vocabulary"
                            question = random.choice(vocab) #randomly selects a question out of 5 from the file
                            print("\n",question) #prints question
                            vocab.remove(question) #removes question from list
                            guess = input("\nWhat is: ").lower() #user guesses answer

                        elif player_choice == 'syntax': #user_input == "syntax"
                            question = random.choice(syntax) #randomly selects a question out of 5 from the file
                            print("\n",question) #prints question
                            syntax.remove(question) #removes question from list
                            guess = input("What is: ").lower() #user guesses answer
                        
                        if error == 1: #If error equals 1 restarts game  
                            print("restarting game...")
                        else:
                            #opens answers to check if guess is wrong or right
                            with open("answers.txt") as answers:
                                list_answers = answers.readlines() #assigns list_answers to the file "answers"
                                for a in range(len(list_answers)): #checks the list amount of answers for a
                                    if guess == list_answers[a][:-1]: #Checks if guess equals an answers in "answers" file 
                                        flag = 1 # adss 1 to flag
                                        print("Correct!") #User is right
                                        add_score(selected_player,points) #passes plaer and adds points requested by user 
                                        questions_answered += 1 #questions is added by 1 
                                    
                                if flag == 0: #Checks if flag is 0
                                    print("Incorrect!") #User guess is wrong
                                    questions_answered += 1 #questions is added by 1 
                                    subtract_score(selected_player,points) #passes plaer and subtracts points requested by user
                                
                        trivia = random.choice(funFacts) #randomly selects a line from the list in funFacts
                        print("\n",trivia) #prints out the fact     
                        input(raw_input)
                        clear_screen()
            #selects player name and score from dict file "players_stats
            for k, v in players_stats.items(): 
                print(k,v) #prints player name and score
                if max < v: #checks if score is bigger than Max
                    max = v #sets score to max
                    player = k #player name is assigned to variable "player"

            print("The winner is",player) #Prints out the highest scorer in the game
        # add questions
        if selection == 2:
            player_choice = input("Please enter a category to add a question (code,vocabulary, syntax): ")#ask player to add a question
            if player_choice == "code":
                codeA = open("code.txt","a")#opens code file
                new_question = input("Please enter your new question: ")#ask for new question
                codeA.write(new_question+ "\n")#appends new question
                codeA.close()#closes file
                max_questions += 1#addes 1 to max questions

                answersA = open("answers.txt","a") #opens answers file
                new_answer = input("Please enter your new answer: ") #ask for new answer
                answersA.write(new_answer+ "\n")#appends new answer
                answersA.close()#closes answer
                
            elif player_choice == "vocabulary":
                vocabA = open("vocab.txt","a")#opens vocab file
                new_question = input("Please enter your new question: ")#ask for new question
                vocabA.write(new_question+ "\n")#appends new question
                vocabA.close()#closes file
                max_questions += 1#addes 1 to max questions

                answersA = open("answers.txt","a") #opens answers file
                new_answer = input("Please enter your new answer: ")#ask for new answer
                answersA.write(new_answer+ "\n")#appends new answer
                answersA.close()#closes answer

                
            elif player_choice == "syntax":
                syntaxA = open("syntax.txt","a")
                new_question = input("Please enter your new question: ")#ask for new question
                syntaxA.write(new_question+ "\n")#appends new question
                syntaxA.close()#closes file
                max_questions += 1#addes 1 to max questions

                answersA = open("answers.txt","a")#opens answers file
                new_answer = input("Please enter your new answer: ")#ask for new answer
                answers.write(new_answer+ "\n")#appends new answer
                answersA.close()#closes answer
            else:
                print("\nError adding question...restarting program")
                
        input(raw_input)
        clear_screen()
        
        #Exits the program
        if selection == 3:
            print("exiting program")
                           
              
main()
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
