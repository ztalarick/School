'''
Created on Oct 27, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the Stevens Honor System.
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

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

def invert(s):
    '''takes a binary string and returns the opposite of each value, ex: 10101 --> 01010'''
    if s == '':
        return ''
    if s[0] == '1':
        return '0' + invert(s[1:])
    return '1' + invert(s[1:])

def TcToNum(s):
    '''takes an 8bit binary string and returns an int'''
    if s[0] == '0':
        return binaryToNum(s)
    return -1 * binaryToNum(increment(invert(s)))

def NumToTc(n):
    '''takes an int and returns it in two's compliment'''
    if n == 0:
        return '0' * 8
    if n > 0:
        binary_n = numToBinary(n)
        number_zeros = 8 - len(binary_n)
        if number_zeros < 0 or n >= 128:
            return 'Error'
        return ('0' * number_zeros) + binary_n
    binary_n = numToBinary(-1 * n)
    num_zeros = 8 - len(binary_n)
    if num_zeros < 0 or n < -128:
            return 'Error'
    tc_binary= (num_zeros * '0') + binary_n
    return increment(invert(tc_binary))

