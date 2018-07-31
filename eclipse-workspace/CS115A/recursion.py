'''
Created on Sep 12, 2017

@author: Zach
'''
from cs115 import  map, reduce, filter
import math

def tower(n):
    if n == 0: 
        return 1 
    return 2 ** tower(n - 1)
        
def tower_reduce(n):
    def power(x, y):
        return y ** x
    if n == 0:
        return 1
    return reduce(power, [2] * n)
    
def length(lst):
    if lst == []:
        return 0
    return 1 + length(lst[1:])
    
def reverse(lst):
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]
    
def member (x, lst):
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1) 

def power_tail(x, y):
    def power_tail_helper(x, y, accum):
        if y ==0:
            return accum
        return power_tail_helper(x, y-1, accum * x)
    return power_tail_helper(x, y, 1)

def mystery(n):
    return mystery_help(n, 0)

def mystery_help(n, r):
    if n == 0:
        return r
    return mystery_help(n // 10, r * 10 + n % 10)

def my_map(f, lst):
    '''returns a new list where the function f is applied to every value in the original list'''
    if lst == []:
        return []
    return f(lst[0]) + my_map(f ,lst[1:])

def my_reduce_helper(f, lst, accum):
    if lst == []:
        return accum
    return my_reduce_helper(f, lst[1:], f(accum, lst[0]))

def my_reduce(f, lst):
    if lst == []:
        raise TypeError("Cannot enter a list with no initial value")
    return my_reduce_helper(f, lst[1:], lst[0])

def prime(n):
    '''returns whether or not an integer is prime'''
    possible_divors = range(2, int(math.sqrt(n)) + 1)
    divors = filter(lambda x: n % x == 0, possible_divors)
    return len(divors) == 0

def primes(n):
    '''returns a list of primes in the range [2, n]  computed via the sieve of erathosthenes'''
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

def fib(n):
    '''returns the nth fibonacci number'''
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)





    













