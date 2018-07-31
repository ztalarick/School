'''
Created on Sep 18, 2017

@author: Zach
'''
from cs115 import *
import sys
sys.setrecursionlimit(10000)
'''Allows up to 10,000 recursive calls'''

Dictionary = ['902', '820', '888', '270', '999', '123', '456', '789', '209', '884', '423', '723', '210']
bonglePoints = [['0', 1.2], ['2', 2.2], ['9', 9.2]]

def is_code_possible(code, numbers):
    if code == '':
        return True
    if code[0] in numbers:
        return (is_code_possible(code[1:], remove(code[0], numbers)))
    else:
        return False
    
def remove(number, numbers):
    if numbers == []:
        return []
    if number == numbers[0]:
        return numbers[1:]
    else:
        return [numbers[0]] + remove(number, numbers[1:])
    
def numberPoints(number, pointslist):
    '''returns the points for a given number'''
    if pointslist == []:
        return 0.0
    first = pointslist[0]
    if first[0] == number:
        return first[1]
    return numberPoints(number, pointslist[1:])

def codePoints(code, pointslist):
    if code == "":
        return 1
    return numberPoints(code[0], pointslist) * codePoints(code[1:], pointslist)

def list_of_code_created(dictionary, numbers):
    return filter(lambda code: is_code_possible(code, numbers) , dictionary)

def pointsList(numbers):
    codes = list_of_code_created(Dictionary, numbers)
    return map(lambda code: [code, codePoints(code, bonglePoints)], codes)

def bestCode(numbers):
    contenders = pointsList(numbers)
    return reduce(lambda x, y: x if x[1] > y[1] else y , contenders)

