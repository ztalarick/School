'''
Created on 9/16/17
@author:    Zachary Talarick
Pledge:    I pledge my honor that I have abided by the Steven's Honor System. ztalaric

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
#from dict import *
from bigdict import *
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]


#Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
#              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    '''returns the score for a given letter'''
    if scorelist == []:
        return 0.0
    first = scorelist[0]
    if first[0] == letter:
        return first[1]
    return letterScore(letter, scorelist[1:])
    
def wordScore(S, scorelist):
    '''returns the score for a given word'''
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
   
def remove(letter, letters):
    ''' removes a letter from a word'''
    #print(letters)
    if letters == []:
        return []
    if letter == letters[0]:
        return letters[1:]
    else:
        return [letters[0]] + remove(letter, letters[1:])
    
def is_word_possible(word, letters):
    ''' tests if a word is possible from the letters given'''
    if word == '':
        return True
    if word[0] in letters:
        return (is_word_possible(word[1:], remove(word[0], letters)))
    else:
        return False

def list_of_word_created(dictionary, letters):
    '''returns a list of the words that are possible from given letters'''
    return filter(lambda word: is_word_possible(word, letters) , dictionary)

def scoreList(rack):
    '''returns a list of all possible words in a dictionary from an input list of letters'''
    words = list_of_word_created(Dictionary, rack)
    return map(lambda word: [word, wordScore(word, scrabbleScores)], words)

def bestWord(rack):
    '''gets highest scoring word from a list of letters'''
    contenders = scoreList(rack)
    if contenders == []:
        return ['', 0]
    return reduce(lambda x, y: x if x[1] > y[1] else y , contenders)
