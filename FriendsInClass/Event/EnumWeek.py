'''
Created on Feb 9, 2012

This is a Enum that represent the 7 days in a week
This Enum is immutable
This class uses the adapter pattern due to the absence of enum in python.
Using parameter in the class as enum tag and a private inner class as an
adapter to represent each tag with methods.

@author: Hunlan for code review
'''
from Util import Utilities
class EnumWeekday:  
    class __EnumAdapter__:
        # This is a string array that maps index to String representation
        __strArr__ = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # This is a string array that maps index to Abbreviated String representation
        __abrevArr__ = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        
        # @param day: The day number between 1 to 7
        # @override
        def __init__(self, day):
            Utilities.checkRange(day, 1, 8)
            self.day = day;
        
        # A Callable method to return the tag number 
        # @override
        def __call__(self):
            return self.day
        
        # @override
        def __eq__(self, o):
            if(o != None and o.__class__ == self.__class__) :
                return self.day == o.day
            else:
                return False
        
        # @override
        def __str__(self):
            return self.__strArr__[self.day - 1]
        
        # returns an abbreviated string representation
        def toAbrevStr(self):
            return self.__abrevArr__[self.day - 1]
        
        # returns a deep copy of the next day
        def nextDay(self):
            if self.day == 1 :
                return EnumWeekday.TUESDAY
            elif self.day == 2 :
                return EnumWeekday.WEDNESDAY
            elif self.day == 3 :
                return EnumWeekday.THURSDAY
            elif self.day == 4 :
                return EnumWeekday.FRIDAY
            elif self.day == 5 :
                return EnumWeekday.SATURDAY
            elif self.day == 6 :
                return EnumWeekday.SUNDAY
            elif self.day == 7 :
                return EnumWeekday.MONDAY
        
        # returns a deep copy of the previous day    
        def prevDay(self):
            if self.day == 1 :
                return EnumWeekday.SUNDAY
            elif self.day == 2 :
                return EnumWeekday.MONDAY
            elif self.day == 3 :
                return EnumWeekday.TUESDAY
            elif self.day == 4 :
                return EnumWeekday.WEDNESDAY
            elif self.day == 5 :
                return EnumWeekday.THURSDAY
            elif self.day == 6 :
                return EnumWeekday.FRIDAY
            elif self.day == 7 :
                return EnumWeekday.SATURDAY
            
            
    '''Monday to Sunday are the Enum tags with integer value from 1 to 7 respectively'''        
    MONDAY = __EnumAdapter__(1)
    TUESDAY = __EnumAdapter__(2)
    WEDNESDAY = __EnumAdapter__(3)
    THURSDAY = __EnumAdapter__(4)
    FRIDAY = __EnumAdapter__(5)
    SATURDAY = __EnumAdapter__(6)
    SUNDAY = __EnumAdapter__(7)
    
    @staticmethod
    def fromInt(i):
        Utilities.checkRange(i, 1, 8)
        if i == 1 :
            return EnumWeekday.MONDAY
        elif i == 2 :
            return EnumWeekday.TUESDAY
        elif i == 3 :
            return EnumWeekday.WEDNESDAY
        elif i == 4 :
            return EnumWeekday.THURSDAY
        elif i == 5 :
            return EnumWeekday.FRIDAY
        elif i == 6 :
            return EnumWeekday.SATURDAY
        elif i == 7 :
            return EnumWeekday.SUNDAY

    