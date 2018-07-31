'''
Created on Sep 29, 2017

@author: Zachary Talarick
I pledge my honor I have abided by the Stevens Honor System.
'''

def knapsack(capacity, itemList):
    '''returns how the capacity can be filled to provide the most value'''
    if capacity == 0 or itemList == []:
        return [0, []]
    
    lose_it = knapsack(capacity, itemList[1:])
    if capacity - itemList[0][0] < 0:
        return lose_it
    use_it =  knapsack(capacity - itemList[0][0], itemList[1:])
    new_use = [itemList[0][1] + use_it[0], [itemList[0]] + use_it[1]]
    
    if new_use[0] > lose_it[0]:
        return new_use
    return lose_it

print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))
#print(knapsack(20, []))
#print(knapsack(0, [[1, 1000], [2, 3000], [4, 55000]]))

