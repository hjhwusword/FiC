'''# Hunlan for code review
# Depreciated
from EnumWeek import EnumWeekday
from Util import Utilities
from Util import ClassSpecificUtilities

class Time:
    __flyweightTimes__ = dict()
    
    def __init__(self, hour, mini, isPM, day):
        # TODO Check isinstance please
        self.__checkConstructorParameter__(hour, mini, isPM, day)       
        self.hour = hour
        self.mini = mini
        self.isPM = isPM
        self.day = day
          
    def getInstance(self, hour, mini, isPM, day):
        self.__checkConstructorParameter__(hour, mini, isPM, day) 
        key = day()*10000 + isPM*720 + hour*60 + mini
        if(not(key in self.__flyweightTimes__)) :
            self.__flyweightTimes__[key] = Time(hour, mini, isPM, day)
        
        return self.__flyweightTimes__[key]
            
    def __getSize__(self):
        return len(self.__flyweightTimes__)
    
    # should return a new time, dont mutate this class
    def shift(self, amount):
        # shift amount
        totMin = self.__getNormalizeTime__() + amount
        remainderAfterDay = totMin % 1440
        remainderAfterPM = remainderAfterDay % 720
        remainderAfterHour = remainderAfterPM % 60
        
        today = self.day
        while(totMin/1440 != 0):
            today = today.nextDay()
            totMin = totMin - 1440
        
        theIsPM = True if totMin >= 720 else False
        theHour =remainderAfterPM / 60 if remainderAfterPM / 60 != 0 else 12 
        theMini = remainderAfterHour
        
        return Time(theHour,theMini,theIsPM,today)
        
    def getHour(self):
        return self.hour
    
    def getMin(self):
        return self.mini
    
    def getIsPM(self):
        return self.isPM
    
    def getDay(self):
        return self.day
    
    def __getNormalizeTime__(self):
        theTime = 720 if self.isPM else 0
        theTime += (self.hour % 12) * 60 + self.mini
        return theTime

    
    def __checkConstructorParameter__(self, hour, mini, isPM, day):
        Utilities.checkInstanceInt(hour)
        Utilities.checkInstanceInt(mini)
        Utilities.checkInstanceBool(isPM)
        ClassSpecificUtilities.checkInstanceEnumWeek(day)
        Utilities.checkRange(hour, 1, 13)
        Utilities.checkRange(mini,0,60)
    
        
    def __hash__(self):
        return self.__getNormalizeTime__()
        
    # implement this
    def __str__(self):
        return self.day.toAbrevStr() + " " + str(self.hour) + ":" + str(self.mini) + ("PM" if self.isPM else "AM")
    
    # Rich Comparisons
    def __eq__(self, other):
        if(other != None and other.__class__ == self.__class__) :
            return self.hour == other.hour and self.mini == other.mini and self.isPM == other.isPM and self.day == other.day
        else:
            return False
        
    def __lt__(self, other):
        if(other != None and other.__class__ == self.__class__) :
            if(self.day() == other.day()):
                return (self.__getNormalizeTime__() - other.__getNormalizeTime__() < 0)
            return (self.day() - other.day() < 0)
        else :
            raise TypeError("Can not compare different types")
        
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        return not(self.__lt__(other) or self.__eq__(other))
    
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
                
    
    '''