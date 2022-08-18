# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:38:15 2022

@author: Asus
"""

# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import re

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def is_valid_word(word,wordlist):
    if word in wordlist:
        return True
    else:
        return False
    
def can_still_be_a_word(fragment,wordlist):
    wordlist_trim=[]
    for word in wordlist:
        wordlist_trim.append(word[0:len(fragment)])
    
    return is_valid_word(fragment,wordlist_trim)
    

def play_ghost(wordlist):
    print("Time to play some ghost!")
    print("Player one goes first...")
    acumWord="" #presentation
    
    while True: #run until somebody looses
        while True: #verification that input is only one letter from a-z
            Player1=input("Player 1 add your letter: ")
            if not len(Player1)==1 or not re.match("^[a-z]*$",Player1):
                print("Invalid input! enter only one letter from a to z")
            else:
                break
                                
        acumWord+=Player1 #fragment so far
        print("current word fragment is %s\n " %acumWord)
        if is_valid_word(acumWord,wordlist) and len(acumWord)>3: #verifies if the fragment is a word with lenght>3.
            print("'%s' is a word! player 1 looses!" %acumWord)
            break
        elif not can_still_be_a_word(acumWord,wordlist): #verifies if there are any words in the list that start with the current fragment.
            print("there are no words that start with '%s' player 1 looses!" %acumWord)
            break
        else:
            print("it's player's 2 turn!")
            while True:
                Player2=input("Player 2 add your letter: ") # input verification
                if not len(Player2)==1 or not re.match("^[a-z]*$",Player2):
                    print("Invalid input! enter only one letter from a to z")
                else:
                    break
            acumWord+=Player2 #new fragment
            print("current word fragment is %s\n " %acumWord)
            if is_valid_word(acumWord,wordlist) and len(acumWord)>3: #loose verification
                print("'%s' is a word! player 2 looses!" %acumWord)
                break
            elif not can_still_be_a_word(acumWord,wordlist):
                print("there are no words that start with '%s' player 2 looses!" %acumWord)
                break
            else:
                print("it's player's 1 turn!") #back to the begining.
            
        
       
