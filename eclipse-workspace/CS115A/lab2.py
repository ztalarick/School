'''
Created on Sep 15, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the Steven's Honor System. ztalaric
'''
from cs115 import map, reduce

def dot(L, K):
    '''returns the dot product of two lists'''
    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])

    
def explode(S):
    '''returns a string as a list'''
    if S == "": 
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    '''Returns the value in a list where the parameter e is equal to it '''
    if L == [] or L == "":
        return 0
    elif e == L[0]:
        return 0  
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''checks if e = any value in a list and returns a new list without e, if there is no e it returns the length of L'''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e, L[1:]) 
    return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    '''applies a function to every value in a list and if the function returns false for a value remove it from the list and return a new list with only True values'''
    if L == []:
        return []
    elif f(L[0]) == False:
        return myFilter(f, L[1:])
    return [L[0]] + myFilter(f, L[1:])

def deepReverse(L):
    '''Returns the reverse of a List and the reverse of any Lists inside the List'''
    if L == []:
        return []
    x = L[0]
    if isinstance(x, list):
        return  deepReverse(L[1:]) + [deepReverse(x)] 
    return deepReverse(L[1:]) + [L[0]]

    








