'''
Created on Sep 7, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the Steven's Honor System.
'''
from cs115 import map, range, reduce
from math import factorial
import math


def add(a, b):
    return a + b #adds 2 numbers

def inverse(n): #This function takes an integer n and returns the reciprocal 1 / n as a float decimal
    return 1 / n

def e(n): #uses a taylor polynomial to approximate e   
    return reduce(add, (map(inverse, (map(factorial, range(0, n+1))))))

def error(n): # takes the actual value of e and subtracts it from the approximated value
    return math.e - abs(e(n))

print(e(10))

print(error(1))

