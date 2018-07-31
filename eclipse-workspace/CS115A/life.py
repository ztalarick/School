#
# life.py - Game of Life lab
#
# Name:
# Pledge:
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''returns a 2D array with width rows and height columns'''
    col = []
    for row in range(height):
        col.append(createOneRow(width)) 
    return col

def printBoard( A ):
    """ this function prints the 2d list-of-lists
     A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width, height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width, height):
    '''makes a 2 array of all boarders being 0 and all inervales being 1'''
    A = createBoard(width, height)
    for row in range(width - 1):
        for col in range(height - 1):
            if row != 0 and col != 0:
                A[row][col] = 1
    return A

def randomCells(width, height):
    '''creates a 2d array with all boarders being 0 and all inner vales being a random 1 or 0'''
    A = createBoard(width, height)
    for row in range(width - 1):
        for col in range(height - 1):
            if row !=0 and col != 0:
                A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    '''makes a copy of L when there are lists inside of lists. stores all lists in seprate memory location'''
    M = []
    for x in A:
        if type(x) is list:
            M.append(copy(x))
        else:
            M.append(x)
    return M

def innerReverse( A ):
    '''reverses all the interior values of 2d array A'''
    newA = copy(A)  
    for row in range(len(A) - 1):
        for col in range(len(A[row]) - 1):
            if row != 0 and col != 0:
                if A[row][col] == 0:
                    newA[row][col] = 1
                else:
                    newA[row][col] = 0      
    return newA

def count_neighbors(row, col, A):
    '''returns the number of bordering live cells'''
    neighbors = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if A[r][c] == 1:
                neighbors += 1
    if A[row][col] == 1:
        neighbors -= 1
    return neighbors
        
    

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A)  
    for row in range(len(A) - 1):
        for col in range(len(A[row]) - 1):
            if row != 0 and col != 0:
                if count_neighbors(row, col, A) < 2 or count_neighbors(row, col, A) > 3: 
                    newA[row][col] = 0
                elif count_neighbors(row, col, A) == 3:
                    newA[row][col] = 1
    return newA

nb = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
print(count_neighbors(2, 1, nb))
printBoard(next_life_generation(nb))