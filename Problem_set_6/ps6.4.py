# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:38:15 2022

@author: Asus
"""
# Problem Set 6: 6.00 Word Game
# Name: Word Game
# Collaborators: 
# Time: 
#
import time
from itertools import combinations
import copy
import random
from math import ceil
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

word_list = load_words()

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n): #DONE!
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    totalPoints=0;
    for letter in word:
        #print(SCRABBLE_LETTER_VALUES[letter])
        totalPoints+=SCRABBLE_LETTER_VALUES[letter];
    if len(word)==n:
        totalPoints+=50;
        
    return totalPoints;
        
    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand): 
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter, end =" ")             # print all on the same line
    print ()                             # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = max(ceil(n / 3),1) #range can't be a float.
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word): #DONE!
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    newHand=hand.copy()
    for letter in word:
        newHand[letter]=newHand[letter]-1;
        
    return newHand
    

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    isValid=True
    for letter in word:
        if letter not in hand.keys():
            return False
        
    if word not in word_list:
        return False
    
    newHand=update_hand(hand,word) #assuming it has all the letters, if one of them end up being negative, it means there were not enough letters.
    
    for key in newHand:
        if newHand[key]<0:
            return False
    
    return isValid
            

#
# Problem #4: Playing a hand
#
def get_words_to_points(word_list):
    points=[get_word_score(word, HAND_SIZE) for word in word_list];
    points_dict=dict(zip(word_list, points))
    return points_dict
    
points_dict=get_words_to_points(word_list)
 
def get_time_limit(points_dict, k): #calculates a maximum reasoable time to expect from the computer.
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    words=list(points_dict.keys())
    for word in words:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

#time_limit=get_time_limit(points_dict, 1)

def sort_hand(hand): #convers the hand dictionary into a sorted string,   {'w': 2, 'i': 1, 'n': 1, 'd': 1, 'o': 1, 's': 1} returns  'dinosww'
    letters=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            letters.append(letter)
    sortedHand=''.join(sorted(letters))
    return sortedHand
        
    
def get_word_rearrangements(word_list): #returns a sorted dictionary for each word. {sortedword: word} ej {'dinosww':'windows'}
    
    sortedWords=[''.join(sorted(word)) for word in word_list]

    rearrange_dict=dict(zip(sortedWords,word_list))

    return rearrange_dict

def build_substrings(handString): #returns all possible combinations of strings with a given set of letters, ej "abc", returns ['bc', 'abc', 'c', 'ac', 'b', 'ab', 'a'], since we are comparing sorted strings, "cab" or "bac" are ignored
    substrings=[]
    for i in range(1,len(handString)+1): 
        aux=[''.join(c) for c in combinations(handString,i)]; #combinations of the letters, using from 1 to all.
        substrings.extend(aux)
    
    return list(set(substrings))
        
    

def pick_best_word_fast(hand,rearrange_dict): #instead of points_dict, it is going to use rearrangement_dict
    bestScore=0;
    bestWord=""
    sortedHand=sort_hand(hand) #returns a sorted string of the hand
    subset=build_substrings(sortedHand) #returns all possible combinations of words with the given hand.
    
    for word in subset:
        sortedWord=''.join(sorted(word))
        if sortedWord in rearrange_dict and get_word_score(sortedWord,HAND_SIZE)>bestScore: #If the word, exists on the list, and the score is higher than the highest so far.
            bestScore=get_word_score(sortedWord,HAND_SIZE) #the score of the sorted word is the same as the score of the actual word.
            bestWord=rearrange_dict[sortedWord]
            
    if bestWord=="":
        print("there are no words possible")
        return "."
    else:
        return bestWord #, bestScore


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    totalPoints=0
    print("--------------------")
    print("Welcome to WORDGAME!")
    print("--------------------")
    print("This is your hand")
    
    display_hand(hand)
    
    remaining_time=get_time_limit(points_dict, 1) # secconds to play in total
    start_timer=time.time() #start timer time
    start_time = time.time() #start time
    rearrange_dict=get_word_rearrangements(word_list)
    #word=input("enter your word: ") #Instead of input, it picks the best word possible
    word=pick_best_word_fast(hand,rearrange_dict) #only picks from possible permutations.
    print("enter your word: "+ word)
    
    keepPlaying=True
    while keepPlaying:
        if not is_valid_word(word,hand,word_list):
            if word==".": #finish playing
                print("you want to leave, ah? Shame!, your total score is %0.2f" %totalPoints)
                break
            
            print("the word you entered is not valid, try anotherone!\nor enter . to finish")
            end_timer=time.time() #end timer
            remaining_time=remaining_time-(end_timer-start_timer)
            print("you have %0.2f seconds left" %max(0,remaining_time))
            start_timer=time.time()
            if remaining_time<0:
                print("oops! it looks like you run out of time, your total score is %0.2f" %totalPoints)
                break

            print("--------------------")
            print("This is your hand")
            
            display_hand(hand)
            #word=input("enter your word: ") #Instead of input, it picks the best word possible
            word=pick_best_word_fast(hand,rearrange_dict)
            print("enter your word: "+ word)
        else:
            end_time = time.time() #end time
            total_time = end_time - start_time #time passed
            
            end_timer=time.time() #end timer
            remaining_time=remaining_time-(end_timer-start_timer)      
            
            print ('It took %0.2f to enter your word' % max(0.01,total_time)) #if it rounds to zero, then it takes 0.01 as minimum time.
            print("you have %0.2f seconds left" %max(0,remaining_time)) #timer total
            if remaining_time<0:
                print("oops! it looks like you run out of time, your total score is %0.2f" %totalPoints)
                break
            totalPoints+=get_word_score(word,HAND_SIZE)/max(0.01,total_time) #se añade puntaje sobre tiempo. si el tiempo es 1. no se resta
            if len(word)==HAND_SIZE:
                print("Nois! you used all your letters in one word! + 50 points!")
                print("'%s' is hell of a good one, now you have %0.2f points!" %(word,totalPoints))
            else:
                print("'%s' is a nice one, now you have %0.2f points!" %(word,totalPoints))
        
            hand=update_hand(hand, word)
            if sum(hand.values())==0:
                print("great! You used all your letters!")
                keepPlaying=False
            else:
                print("--------------------")
                print("This is your hand")
                display_hand(hand)
                start_time = time.time() #start time
                start_timer=time.time() #start timer again
                #word=input("enter your word: ") #Instead of input, it picks the best word possible
                word=pick_best_word_fast(hand,rearrange_dict)
                print("enter your word: "+ word)
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    #print ("play_game not implemented.")         # delete this once you've completed Problem #4
    #play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    # uncomment the following block of code once you've completed Problem #4
    #hand=get_frequency_dict( 'dinosww')
#    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
#            hand = deal_hand(HAND_SIZE)
            hand=get_frequency_dict( 'dinosww')
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")


# Build data structures used for entire session and play game
#
#if __name__ == '__main__':

play_game(word_list)

"""
--------------------
Welcome to WORDGAME!
--------------------
This is your hand
u o e x g r p 
enter your word: expo
It took 0.16 to enter your word
you have 0.09 seconds left
'expo' is a nice one, now you have 83.24 points!
--------------------
This is your hand
u g r 
enter your word: rug
It took 0.16 to enter your word
you have 0.00 seconds left
oops! it looks like you run out of time, your total score is 83.24

"""


