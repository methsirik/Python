# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:12:00 2021

@author: Methsiri_07324
"""
import random

def get_ratings(file_name, usr_name):  # file name of the ratings
    dic_1 = {}
    file = open(file_name, 'r')
    list_1 = file.read().splitlines(keepends=False)
    file.close()
    for line in list_1:
        x, y = line.split()
        dic_1[x] = int(y)
    if usr_name in dic_1:
        return dic_1[usr_name]
    else:
        return 0

def default_game(user_input):  # input string
    aval_choices = ["rock", "paper", "scissors"]
    win_comb = ["rock_scissors", "paper_rock", "scissors_paper"]
    random.seed()
    comp_choice = random.choice(aval_choices)
    if user_input in aval_choices:
        comb_string = user_input + "_" + comp_choice
        if user_input == comp_choice:
            return "draw", comp_choice
        elif comb_string in win_comb:
            return "win", comp_choice
        else:
            return "lost", comp_choice
    else:
        return "Invalid", comp_choice

def list_game(user_input, input_list):
    random.seed()
    comp_choice = random.choice(input_list)
    if user_input in input_list:
        l = len(input_list) - 1
        n = l // 2
        m = input_list.index(user_input)
        if m > n:
            win_list = input_list[(m + 1):] + input_list[:(n - (l - m))]
        elif m < n:
            win_list = input_list[(m + 1):(m + 1 + n)]
        else:
            win_list = input_list[(n + 1):]
        if comp_choice == user_input:
            return "draw", comp_choice
        elif comp_choice in win_list:
            return "lost", comp_choice
        else:
            return "win", comp_choice
    else:
        return "Invalid", comp_choice

name = input('Enter your name: ')
print('Hello,', name)

rating = get_ratings('rating.txt', name)

input_string = input()
if input_string != "":
    input_list = input_string.split(",")

print("Okay, let's start")

while True:
    usr_input = input()
    if usr_input == "!exit":
        break
    elif usr_input == '!rating':
        print("Your rating:", rating)
    else:
        if input_string == "":
            status, comp_choice = default_game(usr_input)
        else:
            status, comp_choice = list_game(usr_input, input_list)
            
        if status == 'win':
            print(f"Well done. The computer chose {comp_choice} and failed")
            rating += 100
        elif status == 'draw':
            print(f"There is a draw ({comp_choice})")
            rating += 50
        elif status == "lost":
            print(f"Sorry, but the computer chose {comp_choice}")
        else:
            print("Invalid input")
            
print("Bye!") 
