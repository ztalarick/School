'''
Created on Sep 18, 2017

@author: Zach
'''
from cs115 import *

def powerset(lst):
    '''returns the power set of the list, that is the set of all subsets of the list'''
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [list[0]] + subset, lose_it)
    return lose_it + use_it

def subset(target, lst):
    '''determines whether or not it is possible to create a target sum from values in a list'''
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target, lst):
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])     
    return subset_with_values(target, lst[1:])

def LCS(S1, S2):
    '''returns the length of the longest common substring of strings S1 and S2'''
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def LCS_with_values(S1,S2):
    if S1 == '' or S2 == '':
        return (0, ' ')
    if S1[0] == S2[0]:
        result = LCS_with_values(S1[1:], S2[1:])
        return (1 + result[0], S1[0] + result[1]) 
    useS1 = LCS_with_values(S1, S2[1:])
    useS2 = LCS_with_values(S1[1:], S2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2 

def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values (lst):
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it [0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

def distance(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    subsituton = distance(first[1:], second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first, second[1:])
    return 1 + min(subsituton, deletion, insertion)


    
    
    
    
    








