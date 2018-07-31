'''
Created on Oct 3, 2017

@author: Zachary Talarick
'''
from cs115 import range


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})
    
'''if the key is in the memo return the value associated with the key
do work use recursion to compute your answer but store the result in a local variable
put the result in the memo and then return the result'''

def LCS_memo(S1, S2):
    '''returns the length of the longest common substring of strings S1 and S2'''
    def LCS_helper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        
        if S1 == '' or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + LCS_helper(S1[1:], S2[1:], memo)
        else:
            result = max(LCS_helper(S1, S2[1:], memo), LCS_helper(S1[1:], S2, memo))
        memo[S1, S2] = result
        return result
    return LCS_helper(S1, S2, {})


def subset_memo(target, lst):
    '''determines whether or not it is possible to create a target sum from values in a list'''
    def subset_helper(target, lst, memo):
        if (target, lst) in memo:
            return memo[(target, lst)]
        if target == 0:
            result = True
        elif len(lst) == 0:
            result = False
        else:
            result = subset_helper(target - lst[0], lst[1:], memo) or subset_helper(target, lst[1:], memo)
        memo[(target, lst)] = result
        return result
    return subset_helper(target, lst, {})

print(subset_memo(100000, tuple(range(1, 900))))