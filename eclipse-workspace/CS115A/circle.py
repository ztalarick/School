'''
Created on Nov 21, 2017

@author: Zach
'''
from shape import shape
import math

class Circle(shape):
    def __init__(self, x, y, radius, name = 'Circle'):
        super().__init__(x, y, name)
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        self.__radius
    
    @property
    def area(self):
        return math.pi * (self.__radius) ** 2 
    
    def __str__(self):
        return super().__str__() + ', Radius = ' + str(self.__radius) + ', Area = ' + str(self.area)

if __name__ == '__main__':
    c = Circle(10, 10, 10)  
    print(c)
    
    
