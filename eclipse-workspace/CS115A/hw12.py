'''
Created on Dec 3, 2017

@author: Zachary Talarick
I pledge my honor that I have  abided by the Stevens Honor system. ztalaric
'''
from cs115 import range


class Board(object):
    def __init__(self, width = 7, height = 6):
        self.__width = width
        self.__height = height
        
        self.__board = []
        
        '''
        for i in range(width):
            self.__board.append([])
            for j in range(height):
                self.__board[i].append(' ')
        '''
        for i in range(height):
            self.__board.append([' '] * self.__width)
        
    def __str__(self):
        result = '|'
        for row in range(len(self.__board)):   
            for col in range(self.__width):
                result += self.__board[row][col] + '|'
            result += '\n|'
        result = result[:-2]
        result += '\n' + (((self.__width*2) +1) * '-') + '\n' 
        for x in range(self.__width):
            result += ' ' + str(x)
        
        return result
    
    def allowsMove(self, col):
        '''returns a bool determining if the column is empty'''
        count = 0
        for row in self.__board:
            if row[col] != ' ':
                    count += 1
        if count < self.__height:
            return True
        return False
    
    def addMove(self, col, ox):
        '''adds the move to the board'''
        if ox == 'X' or ox == 'O':
            if self.allowsMove(col) == True:
                for row in range(len(self.__board)):
                    if self.__board[row][col] != ' ':
                        self.__board[row - 1][col] = ox
                        break
                    elif self.__board[row][col] == ' ' and row == self.__width - 2: 
                        self.__board[self.__height - 1][col] = ox  
            
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
                if nextCh == 'X': 
                    nextCh = 'O'
                else: nextCh = 'X'

    
    def delMove(self, col):
        '''deletes the top x or o in a column'''
        if self.allowsMove(col) == True:
            for row in range(len(self.__board)):
                if self.__board[row][col] != ' ':
                    self.__board[row][col] = ' '
                    break
                    
    def winsFor(self, ox):
        '''returns a bool determining if anyone wins on the current board state'''
        for directionx, directiony in [[1, -1], [1, 1], [1, 0], [0, 1]]:
            for row in range(len(self.__board)):
                for col in range(self.__width):
                    count = 0
                    for check in range(self.__width):
                        if row + check * directiony >= self.__height or col + check * directionx >= self.__width:
                            break
                        current = self.__board[row + check * directiony][col + check * directionx]
                        if current == ox:
                            count += 1
                        else:
                            count = 0
                        if count >= 4:
                            return True
        return False
                        
                    
                    
               
    def hostGame(self):
        print('Welcome to Connect Four!')
        print(self.__str__())
        i = 1
        while self.winsFor('X') == False and self.winsFor('O') == False:
            ySkip = False
            if i > self.__width * self.__height:
                print("The game is a draw.")
                break
                
            if i % 2 != 0:
                #do X
                userInput = input("X's choice: ")
                try:
                    userInput = int(userInput)
                except:
                    print("Error, not a number")
                
                if userInput < self.__width and self.allowsMove(userInput) == True:
                    self.addMove(userInput, 'X')
                else:
                    print('Error not a valid column.')
                    i -= 1
                    ySkip = True
            if i % 2 == 0 and ySkip == False:
                #do Y
                userInput = input("O's choice: ")
                try:
                    userInput = int(userInput)
                except:
                    print("Error, not a number")
                if userInput < self.__width and self.allowsMove(userInput) == True:
                    self.addMove(userInput, 'O')
                else:
                    print('Error not a valid column.')
                    i -= 1
            i += 1   
                                 
            print(self.__str__())
            
        winner = ''
        if self.winsFor('X') == True:
            print('X wins -- Congratulations!')
        elif self.winsFor('O') == True:
            print('O wins -- Congratulations!')
    
if __name__ == "__main__":
    board = Board(7, 6)
    board.hostGame()



    
        
        
        