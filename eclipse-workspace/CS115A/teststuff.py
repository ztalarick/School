'''
Created on Dec 5, 2017

@author: Zach
'''
'''
count = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        count += i

print(count)
'''
import time

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

start = time.clock()
sum = 0
for x in range(34):
    val = fib(x)
    if val < 4000000000 and val % 2 == 0:
        sum += val
        
print(sum)
end = time.clock() - start
print(end)
