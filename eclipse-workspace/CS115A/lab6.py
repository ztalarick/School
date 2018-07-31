'''
Created on 10/12/2017
@author:   Zachary Talarick
Pledge:   I pledge my honor that I have abided by the Stevens Honor System. ztalaric

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

'''
42 in binary = 101010 = 0 *2^0 + 1 * 2^1 + 0* 2^2 + 1 * 2^3 + 0 * 2^4 + 1 * 2^5
If n is odd the rightmost digit will be a 1 and if even will be a 0. That digit represents 2^0 or 1 and all other digits represent 
a multiple of 2
add up a bunch of powers of 2 reducing the powers by 1
Eliminating the last digit the last digit of a binary number will divide the binary number  by 2 and drop the remainder
'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned. '''
    if n == 0:
        return ''
    elif isOdd(n) == True:
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'           

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    n = len(s)
    return (int(s[0]) * (2 ** (n - 1))) + binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    n = numToBinary((int(binaryToNum(s)) + 1))
    L = (8 - len(n)) * '0' + str(n)
    return L[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return 
    count(increment(s), n - 1)

'''
Ternary value of 59 is 2012 = 2 * 3^0 + 0 * 3^1 + 1 * 3^2 + 2 * 3^3
'''

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n // 3 == 0:
        return str(n % 3)
    return numToTernary(n // 3) + str(n % 3) 

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    n = len(s)
    return (int(s[0]) * (3 ** (n - 1))) + ternaryToNum(s[1:])
