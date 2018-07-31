'''
Created on Nov 17, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the stevens honor system. ztalaric
'''
from dis import dis

class QuadraticEquation(object):
    
    def __init__(self, a, b, c):
        
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")  
    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    
    def root1(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b + discriminant ** (1/2)) / (2 * self.__a)
    
    def root2(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b - discriminant ** (1/2)) / (2 * self.__a)
    
    def __str__(self):
        a = str(self.__a) + 'x^2'
        b = ' + '  + str(self.__b) + 'x'
        c = ' + '+ str(self.__c)
        if self.__a < 0:
            a = '-' + str(-1 * self.__a) + 'x^2'
        if self.__b < 0:
            b = ' - '  + str(-1 * self.__b) + 'x'
        if self.__c < 0:
            c = ' - ' + str(-1 * self.__c)
        if self.__b == 0:
            b = ''
        if self.__c == 0:
            c = ''
        if self.__a == 1:
            a = 'x^2'
        if self.__b == 1:
            b = ' + ' + 'x'
        if self.__a == -1:
            a = a = '-x^2'
        if self.__b == -1:
            b = ' - x'
        return a + b + c + ' = 0'

if __name__ == '__main__':
    qe = QuadraticEquation(-1.0, -5.0, -6)
    print(str(qe))
        

        
        
        
    