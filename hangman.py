#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:05:32 2020

A basic implementation of Hangman game

@author: tamerberk
"""

import random

FILENAME = 'wordlist.txt'
MAX_NUMBER_OF_TRIES = 10


def load_words(filename):
    """
    Reads words from the library file.
    each word in the file has to be in a seperate line
    Args:
        (str) filename - The name of the file
    Returns:
        (list) the list of words
    """
    word_list = []
    try:
        with open(filename, 'r') as file:
            line = file.readline()
            while(line):
                if line:
                    word_list.append(line.strip().lower())
                line = file.readline()
    except Exception as exp:
        print('Error: {}'.format(exp))
    return word_list


def get_a_word(word_list):
    """
    Picks up a word from the word list
    Args:
        (list) word_list - The list of words
    Returns:
        (str) randomly selected word
    """
    return (word_list[random.randint(0, len(word_list)-1)])
    

def read_character():
    """
    Read a character from keyboard
    Returns:
        (str) entered character
    """
    return_char = ''  
    while (return_char==''):
        try:
            char = input('?> ').lower()
            if len(char)!=1:
                print('Error: You can only enter one character',end='')
            else:
                return_char=char
        except Exception as exp:
            print("Error : {}".format(exp))
    return return_char

def read_input(message, options):
    """
    Display a message and ask user to enter a response.
    Response will be one of the given alternatives
    Args:
        (str)  message - A message/question that will be displayed/asked
        (list) options - List of possible options
    Returns:
        (str) randomly selected word
    """
    one_more_time = True
    while (one_more_time):
        try:    
            data = input(message).lower().split()[0]
            for char in options:
                if char == data:
                    one_more_time = False
                    break
        except Exception as exp:
            print('Error: '.format(exp))
    return data

def display_word(message, characters):
    """
    Displaya a message and a word
    This is to diplay the characters of a word one by one.
    Args:
        (str)  message - A message/question that will be displayed/asked
        (str) characters - The word that will be displayed
    Returns:
        (str) randomly selected word
    """    
    print(message, end='')
    for chr in characters:
        print(chr, end='')

def analyze_char(guess,selected_word, used_characters, displayed_characters):
    """
    Anayzes the user entry. First checks if this is already entered.
    Second if this is one of the characters in the selected word. If yes
    returns the position(s) of this letter in the word
    Args:
        (str)  guess - A letter (user's entry)
        (str)  selected_word - The word user is looking for
        (list) used_chaacters - List of already used characters
        (list) displayed_characters - List of characters that are displayed
    Returns:
        (list) list of locations.  -1: Not found, -2: Already used, other:
            location(s) of letters 
    """
    positions=[]
    if guess in used_characters or guess in displayed_characters:
        positions.append(-2)
    else:
        for index in range(len(selected_word)):
            if guess==selected_word[index]:
                positions.append(index)
        if len(positions) == 0:
            positions.append(-1)
    return positions

def check_won_condition(displayed_characters):
    """
    Checks if all letters are found by the user
    Basically there should not be any '*' in the word
    Args:
        (str)  dispayed_characters - The displayed characters of the word
    Returns:
        (boolean) True: won, False: Not won
    """
    won=True
    for index in range(len(displayed_characters)):
        if displayed_characters[index]=='*':
            won=False
            break
    return won

def print_welcome_message(number_of_words):
    """
    Displays a welcome message 
    """
    print('-'*40)
    print('Welcome to Hangman game.')
    print('Words are loaded. There are {} words in the library'.format(number_of_words))
    print('You can make maximum {} guesses'.format(MAX_NUMBER_OF_TRIES))
    print('-'*40)
 

def main():
    """
    The main module. Game logic is in this module
    """
    word_list = load_words(FILENAME)
    if len(word_list)==0:
        print('No words to guess. Terminating the program')
        return
    print_welcome_message(len(word_list))   
    game_continue = 'y'
    reset_game=True
    while game_continue=='y':
        if reset_game:
            game_continue = read_input('Do you want to start?(y/n)', ['y','n'])
            if (game_continue=='y'):
                selected_word=get_a_word(word_list)
                displayed_characters = ['*' for i in range(len(selected_word))]
                used_characters = []
                number_of_tries=0
                reset_game=False  
            else:
                break
        display_word('', displayed_characters)
        if len(used_characters)>0:
            print()
            display_word('Used characters:', used_characters)
        guess = read_character()
        positions = analyze_char(guess, selected_word, used_characters, displayed_characters)
        if positions[0] == -1:
            number_of_tries+=1
            print('Wrong guess! Remaining number of tries : {}'.format(MAX_NUMBER_OF_TRIES-number_of_tries))
            used_characters.append(guess)
        elif positions[0]==-2:
            print('Already entered!')
        else:
            print('Good guess.')
            for index in positions:    
                displayed_characters[index]=selected_word[index]
        if check_won_condition(displayed_characters):
            print('-'*40)
            print('Congratulations. You found it in :)')
            reset_game=True
        elif number_of_tries == MAX_NUMBER_OF_TRIES:
            print('-'*40)
            print ('You could not find it in {} tries'.format(number_of_tries))
            print ('You LOST the game :(')
            print('The word was : {}'.format(selected_word))
            reset_game = True
  
if __name__ == '__main__':
    main()
    






