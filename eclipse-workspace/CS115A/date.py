'''
Created on November 21 2017
@author:   Zachary Talarick
Pledge:    I pledge my honor that I have abided by the stevens honor system. ztalaric

CS115 - Hw 11 - Date class
'''

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
    
    def tomorrow(self):
        '''changes the called object to be one calendar day after it'''
        days = DAYS_IN_MONTH[self.month]
        if self.day == days: 
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            elif self.month == 2 and self.isLeapYear():
                self.day = 29
            else:
                self.month += 1
        elif self.isLeapYear() == True and self.day == 29 and self.month  == 2:
            self.day = 1
            self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        '''changes the object to be the previous calendar day'''
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.year -= 1
                self.day = DAYS_IN_MONTH[self.month]
            elif self.month == 3 and self.isLeapYear() == True:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month] + 1
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
            
    def addNDays(self, n):
        '''changes the object to be n calendar days later'''
        print(self)
        for i in range(n):
            self.tomorrow()
            print(self)
            
    def subNDays(self, n):
        '''changes the object to be n calendar days previous'''
        print(self)
        for i in range(n):
            self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        '''tests if the object is before d2'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False 
        
    def isAfter(self, d2):
        '''tests if the object is after d2'''
        if self.equals(d2) == True:
            return False
        return not self.isBefore(d2)
    
    def diff(self, d2):
        '''returns the difference in days between the object and d2'''
        if self.equals(d2) == True:
            return 0
        
        copy = self.copy()
        count  = 0
        
        while copy.isBefore(d2):
            copy.tomorrow()
            count -= 1
        while copy.isAfter(d2):
            copy.yesterday()
            count +=1
        return count    
    
    def dow(self):
        '''returns the day of the week of the given object'''
        weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        d2 = Date(11, 19, 2017)
        
        n = self.diff(d2) % 7 
        return weekday[n]








