import os
import random

def answers_read():
    answers = open("answers.txt","r")
    ar = answers.readlines()
    answers.close()
    return ar

def code_read():
    code = open("code.txt","r")
    cr = code.readlines()
    code.close()
    return cr

def vocab_read():
    vocab = open("vocab.txt","r")
    vr = vocab.readlines()
    vocab.close()
    return vr

def syntax_read():
    syntax = open("syntax.txt","r")
    sr = syntax.readlines()
    syntax.close()
    return sr

def clear_screen():
    if os.name == "posix":
        clear_cmd = "clear"
    elif os.name == "nt":
        clear_cmd = "cls"
    else:
        print ("\n" * 10)
    os.system(clear_cmd)

def instructions():
    print(
"""
The instructions for Jeopardy are quite simple... There are several categories
that, contain 5 questions each worth double and selected randomly. For this
Jeopardy there will be 3 categories and 5 questions each. The player(s) are to
select a category and a question then,guess it. If the player guesses
incorrectly they have the question points subtracted from their points.
"""
    )

def random_players(names):
    selected_player = random.choice(names)
    return selected_player

def fun_Facts():
    funFacts = open("funFacts.txt","r")
    fr = funFacts.readlines()
    funFacts.close()
    return fr
