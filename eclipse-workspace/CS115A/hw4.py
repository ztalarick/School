'''
Created on Sep 29, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the stevens honor system. ztalaric
'''
from cs115 import map, range

def length(lst):
    '''returns the length of a list'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def pascal_row_helper(lst):
    '''returns the adjacent sums of a list'''
    if lst == [] or length(lst) == 1:
        return []
    return [lst[0] + lst[1]] + pascal_row_helper(lst[1:])

def pascal_row(n):
    '''returns the nth row of pascal's triangle'''
    if n == 0:
        return [1]
    elif n == 1:
        return [1 , 1]
    return [1] + pascal_row_helper(pascal_row(n - 1)) + [1]

def pascal_triangle(n):
    '''returns all the rows in pascal's triangle up to n rows'''
    return map(pascal_row, range(0, n + 1))



