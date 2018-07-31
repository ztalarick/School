'''
Created on Oct 31, 2017

@author: Zachary Talarick
'''
from _sqlite3 import Row

def mapSquare(L):
    '''does map(sqr, L) using a loop, squares each  value of a list'''
    result = []
    for x in L:
        result.append(x * x)
    return result     

def findMax(lst):
    '''returns the max value in list'''
    if lst == []:
        return None
    maxVal = lst[0]
    for x in lst:
        if x > maxVal:
            max_val = x       
    return max_val

def findMax2(lst):
    max_val = lst[0][0]
    row = column = 0
    for r in range(len(lst)):
        for c in range(len(lst[r])):
            if lst[r][c] > max_val:
                max_val = lst[r][c]
                row = r
                column = c  
    return (max_val, (row, column))
        
def findMinMax(lst):
    '''finds the min and max values in a list returns a tupple (min,max)'''
    if lst == []:
        return None
    maxVal = lst[0]
    minVal = lst[0]
    for x in lst:
        if x > maxVal:
            maxVal = x
        elif x < minVal:
            minVal = x
    return (minVal, maxVal)    

def sequential_search(lst, key):
    for x in range(len(lst)):
        if lst[x] == key:
            return x
    return -1

def shallow_copy(L):
    '''makes a copy of L, but has different pointers '''
    M = []
    for x in L:
        M.append(x)
    return M

def deep_copy(L):
    '''makes a copy of L when there are lists inside of lists. stores all lists in seperate memory location'''
    M = []
    for x in L:
        if type(x) is list:
            M.append(deep_copy(x))
        else:
            M.append(x)
    return M

def create_board(r, c):
    board = []

    for row in range(r):
        row = []
        for _ in range (c):
            row.append(' ')
        board.append(row)
    return board

def create_board_comp(r, c):
    return [[' ' for _ in range(c)] for _ in range(r)]

def display_board(board):
    num_rows = len(board)

    for row in range(num_rows):
        num_cols = len(board[row])
        for col in range(num_cols):
            print(' ' + board[row][col] + '' + '|', end=' ')
        if col < num_cols - 1:
            print('|', end =' ')
        print()
        if row < num_rows - 1:
            print('-' * (num_cols * 4) - 1)
            
def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp 
    
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, min_index, i)
        