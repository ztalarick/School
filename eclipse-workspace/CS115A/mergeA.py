'''
Created on Nov 9, 2017

@author: Zach
'''

def num_matches(lst1, lst2):
    '''returns the number of elements the two lists have in common'''
    lst1.sort()
    lst2.sort()
    i = j = count = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]: 
            count += 1
            #increment both
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            # increment i
            i += 1
        else:
            # increment j
            j += 1
    return count

def keep_matches(lst1, lst2):
    '''returns a list of elements that are in both list 1 and list 2'''
    result = []
    lst1.sort()
    lst2.sort()
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]: 
            result.append(lst1[i]) 
            #increment both
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            # increment i
            i += 1
        else:
            # increment j
            j += 1
    return result

def drop_matches(lst1, lst2):
    '''returns a list of elements that are not in common'''
    
    lst1.sort()
    lst2.sort()
    result = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]: 
            #increment both
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            # increment i
            result.append(lst1[i])
            i += 1
        else:
            # increment j
            result.append(lst2[j])
            j += 1
    while i < len(lst1): # if the lists are different sizes
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    return result


print(num_matches(['a', 'b', 'c'], ['b', 'c', 'e']))
print(keep_matches(['a', 'b', 'c'], ['b', 'c', 'e']))
print(drop_matches(['a', 'b', 'c'], ['b', 'c', 'e']))






