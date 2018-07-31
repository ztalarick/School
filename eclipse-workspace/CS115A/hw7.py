'''
Created on Oct 23, 2017

@author: Zachary Talarick
10/25/17
I pledge my honor that I have abided by the Stevens Honor System. ztalaric
'''
def numToBaseB(n, b):
    '''takes an int and returns the converted str in base b'''
    if n == 0:
        return '0'
    def numToBaseB_helper(n, b):
        if n == 0:
            return ''
        elif n // b == 0:
            return str(n % b)
        return numToBaseB_helper(n // b, b) + str(n % b) 
    return numToBaseB_helper(n, b)

def baseBToNum(s, b):
    '''takes an input string s in base b and returns it as an int in base 10'''
    if s == '':
        return 0
    n = len(s)
    return (int(s[0]) * (b ** (n - 1))) + baseBToNum(s[1:], b)

def baseToBase(b1, b2, sb1):
    '''takes a str sb1 in base b1 and returns sb1 converted into b2'''
    return numToBaseB(baseBToNum(sb1, b1), b2)

def add(s, t):
    '''t and s are binary strings return t + s'''
    return numToBaseB(baseBToNum(s, 2) + baseBToNum(t, 2), 2)

def zeroChopper(s):
    '''takes a binary string s and chops off all zeros in front of the first one ie: "001" becomes "1" '''
    if s == '':
        return ''
    elif s[0] == '0':
        return zeroChopper(s[1:])
    return s

def addB(s, t):
    '''t and s are binary strings return t + s  as a binary str without converting to base 10'''
    s = zeroChopper(s)
    t = zeroChopper(t)
    
    def addB_helper(s, t, carry):
        num = carry
        if (s == '' or t == '') and carry == 0:
            return s + t
        carry = 0
        if t != '' and t[-1] == '1': 
            carry = 1 + num
            num = 1 - num
        if s != '' and s[-1] == '1':
            carry = num
            num = 1 - num
        return addB_helper(s[:-1], t[:-1], carry) + str(num)
    return addB_helper(s, t, 0)

    