'''
Created on Nov 13, 2017

@author: Zachary Talarick
I pledge my honor that I have abided by the stevens honor system. ztalaric
'''

dictionary = {}


menu = \
'''
Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - save and quit
'''

def readData():
    '''reads the data from musicrecplus.txt, sorts it and stores it into a dictionary'''
    with open('musicrecplus.txt', 'r') as data:
        for line in data:
            key, value = line.strip().split(':')
            dictionary[key] = sorted(value.split(','))
    return dictionary
    
def setPreferences(user):
    '''called when user presses 'e' or if the user is not already in the dictionary.
    loops until the user presses enter asking them to enter artists each time adding them to the dictionary 
    '''
    go = True
    while go == True:
        print('Enter an artist that you like (Enter to finish): ')
        Input = input()
        if Input == '' or Input == ' ':
            go = False
            break
        dictionary[user] = Input
        
def compare(lst1, lst2):
    '''takes a value and a list returns the number of times a value appears in a list'''
    count = 0
    for i in lst1:
        count += lst2.count(i)
    return count

def removeSame(lst1, lst2):
    '''removes all values that appear in both lists from list 1'''
    return list(set(lst2) - set(lst1))

def reccomendations(user, dictionary):
    '''checks the user's  preferences with other users and recommends the user artists based off other user's  preferences'''
    Dictionary = dictionary.copy()
    userArtists = Dictionary[user] # list of user's artists 
    Dictionary.pop(user)
    keysToRemove = []
    for users in Dictionary:
        if users[-1] == '$':
            keysToRemove.append(users)

    for user in keysToRemove:
        del Dictionary[user]
        
    otherArtists = list(Dictionary.values()) # list of other user's artists excluding the user and private users
    
    numSimilar = []
    
    for artist in otherArtists:
        numSimilar.append(compare(userArtists, artist))
    
    for x in range(len(numSimilar)):
        if numSimilar[x] == len(userArtists):
            numSimilar[x] = 0
    maxVal = numSimilar.index(max(numSimilar))
    
    return sorted(removeSame(userArtists, otherArtists[maxVal]))
     
def login(username):
    '''gets a user input, if the input isn't a key in the dictionary set the preferences '''
    if username not in dictionary:
        setPreferences(username)
    return username

def showPopular(dictionary):
    '''shows the most popular artists'''
    dict = dictionary.copy()
    values = dict.values()
    checks = {}
    
    for list in values:
        for value in list:
            if value in checks:
                checks[value] += 1
            else:
                checks[value] = 1
    if checks == {}:
        return print('Sorry, no artists found.')
    
    firstMax = max(checks, key = checks.get)
    maxVal = checks[firstMax]
    
    for key in checks:
        if checks[key] == maxVal:
            print(key)
            
def getPopular(dictionary):
    '''shows how popular the popular artists are'''
    dict = dictionary.copy()
    values = dict.values()
    checks = {}
    
    for list in values:
        for value in list:
            if value in checks:
                checks[value] += 1
            else:
                checks[value] = 1
    if checks == {}:
        return 'Sorry, no artists found.'
    firstMax = max(checks, key = checks.get)
    maxVal = checks[firstMax]
    return maxVal
    
def showLikes(dictionary):
    '''shows which user has the most likes'''
    dict = dictionary.copy()
    firstMax = max(dict, key = dict.get)
    maxVal = dict[firstMax]
    
    for key in dict:
        if dict[key] == maxVal:
            print(key)
    
def update(dictionary):
    '''sorts and saves dictionary to the text file'''
    county = 0
    with open('musicrecplus.txt', 'w') as file:
        for key in dictionary: 
            if county == 0:
                file.write(str(key) + ':' + ','.join(str(e) for e in dictionary[key]))
            else:
                file.write('\n' + str(key) + ':' + ','.join(str(e) for e in dictionary[key]))
            county +=1
                    
def main():
    '''calls appropriate functions'''
    readData() 
    print('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    username = input()
    login(username)
    run = True
    while run == True:
        print(menu)
        userInput = input()
        
        if userInput == 'e':
            setPreferences(username)
            
        elif userInput == 'r':
            print(reccomendations(username, dictionary))
            
        elif userInput == 'p':
            showPopular(dictionary)
            
        elif userInput == 'h':
            print(getPopular(dictionary))
            
        elif userInput == 'm':
            print(showLikes(dictionary))
            
        elif userInput == 'q':
            update(dictionary)
            run = False
        elif userInput == '' or userInput == ' ':
            pass
        else:
            print('Error not valid input.')
    
main()