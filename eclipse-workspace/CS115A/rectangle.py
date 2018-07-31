'''
Created on Nov 21, 2017

@author: Zach
'''
from shape import shape

class Rectangle(shape):
    def __init__(self, x, y, l, w, name = 'Rectangle'):
        super().__init__(x, y, name)
        self.__l = l 
        self.__w = w 
    
    @property
    def l(self):
        return self.__l
    @property
    def w(self):
        return self.__w
    @l.setter
    def l(self, l):
        self.__l = l 
    @w.setter 
    def w(self, w):
        self.__w = w 
     
    @property
    def area(self):
        return self.__l * self.__w
    
    def __str__(self):
        return super().__str__() + ', Length = ' + str(self.__l) + ', Width = ' + str(self.__w) + ', Area = ' + str(self.area)

if __name__ == '__main__':
    rect = Rectangle(10, 10, 20, 30)
    print(rect)
    
    
    print(isinstance(rect, Rectangle))
    print(isinstance(rect, shape))
    print(isinstance(rect, object))