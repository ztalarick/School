'''
Created on Sep 8, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the Steven's Honor System. ztalaric

'''
from cs115 import map, range, reduce

def mult(x, y): 
    '''Multiplies 2 parameters'''
    return x * y

def add(x, y): 
    '''Adds 2 parameters'''
    return x+ y

def factorial(n): 
    '''returns n!'''
    return reduce(mult, range(1, n+1))

def mean(L):
    '''returns the mean of a list'''
    return reduce(add, L) / len(L)

def divides(n):
    '''checks if the remainder of one number divided by another number is 0'''
    def div(k):
        return n % k == 0
    return div

def prime(n):
    ''' returns a boolean value that determines if the parameter is prime'''
    if n < 2:
        return False
    else:
        return sum(map(divides(n), range(2, int(n ** (1 / 2)) + 1))) == 0 
    
    

