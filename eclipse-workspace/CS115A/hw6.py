'''
Created on 10/16/17
@author:   Zachary Talarick
Pledge:    I pledge my honor that I have abided by the stevens honor system. ztalaric

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

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

def countRun(S, c, MAX_RUN_LENGTH):
    '''
    takes a string of 0s and ones, the character it is looking for and its max run length
    returns the amount of 0s, 1s in a row
    '''
    if S == '':
        return 0
    if c == S[0]:
        return 1 + countRun(S[1:MAX_RUN_LENGTH], c, MAX_RUN_LENGTH)
    return 0

def compress(S):
    '''
    param s: string to compress
    count the runs in s switching
    from counting runs of zeros to counting
    runs of ones
    return compressed string
    '''
    def compress_help(S, c):
        if S == '':
            return ''
        runlen = countRun(S, c, MAX_RUN_LENGTH)
        runlenBinary = numToBinary(runlen)
        zeros = '0' * (COMPRESSED_BLOCK_SIZE - len(runlenBinary))
        if c == '1':
            nextC = '0'
        if c == '0':
            nextC = '1'
        
        return zeros + runlenBinary + compress_help(S[runlen:], nextC)
    return compress_help(S, '0')

def uncompress(S):
    '''
    param S
    in chuncks of COMPRESSED_BLOCK_SIZE
    convert the binary representation of a number
    in that block into that many 0s or 1s 
    switching from 0s to 1s
    switching from decompressing zeros to decompressing ones
    return decompressed string
    '''
    def uncompress_help(S, c):
        if S == '':
            return ''
        if c == '0':
            nextC = '1'
        elif c == '1':
            nextC = '0'
        first5 = S[:COMPRESSED_BLOCK_SIZE]
        binaryS = binaryToNum(first5) * c
        return binaryS + uncompress_help(S[COMPRESSED_BLOCK_SIZE:], nextC)        
    return uncompress_help(S, '0')

def compression(S):
    '''returns compressed size divided by its original size (length)'''
    return len(compress(S)) / len(S)

 
'''
Largest number of bits able to be compressed:
worst case is 1010101010101 need 5 bits for each one so its 5 * 64 = 320

Compression Ratios:
Pictures that have a large amount of the same color in a row can be compressed very well, but pictures who have alternating colors are 
difficult. 

Professor Lai:
There always needs to be a minimum length string to identify a particular compression in my case it is 5 so even if the string needed to be 
compressed is '0' then the returned string will need to be '00001'If there is a picture with less than 5 of a color in a row the compressed version will come out larger.
'''