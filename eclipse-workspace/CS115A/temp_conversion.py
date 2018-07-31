'''
Created on Sep 5, 2017

@author: Zach
'''
from pip._vendor.pyparsing import line
""""F= 9/5C +32"""
def fahrenheit(celcius): 
    """ returns the input degrees Celsius in Fahrenheit"""
    return 9 / 5 * celcius + 32

def celsius(fahrenheit):
    """ returns the input degrees Fahrenheit in Celsius"""
    return 5 / 9 * (fahrenheit - 32)

"""Call the function below the function definitions."""

c = float(input('Enter degrees in Celsius: '))
f = fahrenheit(c)

#You can print multiple items in one statement if you put a comma after each item it prints a space and then goes on to print the next item.
print(c, 'C=', f, 'F')

# You can print this way too, but allowing exactly two decimal places.

print('%.2f C= %.2f F' % (c , f))

f = float(input('Enter the degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F=', c, 'C')
print('%.2f F= %.2f C' % (f , c))

""" 
Try Composition of Funtions 
Converting a Fahrenheit tempature to Celcius and back to Fahrenheit should give you the original Fahrenheit temperature.
"""
print() #print by itself gives a new line
f=float(input('Enter degrees in Fahrenheit: '))
#Use assert to check the return value is equal to the expected value.
assert fahrenheit(celsius(f)) == f
#No output should be produced unless the assertion fails, which means you have an error either in your code or expectation.
