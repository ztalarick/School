'''
Created on Sep 22, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the Steven's Honor System. ztalaric
'''
from cs115 import *
from math import inf

def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float(inf)
    elif amount < coins[0]:
        return change(amount, coins [1:])
    lose_it = change(amount, coins [1:])
    use_it = 1 + change(amount - coins[0], coins)
    return min(lose_it, use_it)

print(change(48, [1, 5, 10, 25, 50]))
print(change(48, [1, 7, 24, 42]))
print(change(35, [1, 3, 16, 30, 50]))