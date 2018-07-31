'''
Created on Sep 26, 2017

@author: Zach
'''
from math import sqrt, acos, degrees

def dot(L, K):
    '''returns the dot product of two lists'''
    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])


lst = [1, 2, 3, 4, 5, 6]
print(lst[:3])