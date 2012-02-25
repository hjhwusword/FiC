'''
Created on Feb 17, 2012

@author: Hunlan
'''

from django.db import models
import datetime
from Util import ClassSpecificUtilities
from Event.EnumWeek import EnumWeekday

class Time(models.Model):
    time = models.TimeField()
    dayIndex = models.IntegerField(max_length = 1)
    
    @staticmethod
    def getInstance(weekday, hour, mini, sec = 0):
        #check instance of variable
        ClassSpecificUtilities.checkInstanceEnumWeek(weekday)
        newTime = datetime.time(hour,mini,sec)
        databaseList = Time.objects.filter(time=newTime,dayIndex=weekday())
        if(len(databaseList) == 1):
            return databaseList[0]
        else:
            instance = Time(time=newTime,dayIndex=weekday())
            instance.save()
            return instance
        
    @staticmethod
    def removeAll():
        databaseList = Time.objects.all()
        for theTime in databaseList :
            theTime.delete()  
    
    def shift(self, amount):
        totMin = self.__getNormalizeTime__() + amount
        remainderAfterDay = totMin % 1440
        remainderAfterHour = remainderAfterDay % 60
        
        todayIndex = self.dayIndex
        if(totMin/1440 > 0) :
            todayIndex = (((self.dayIndex - 1) + totMin/1440) % 7) + 1
            
        theHour = remainderAfterDay / 60
        theMini = remainderAfterHour
        
        return self.getInstance(EnumWeekday.fromInt(todayIndex), 
                                theHour, theMini)
    
    
    
    def getWeekday(self):
        return EnumWeekday.fromInt(self.dayIndex)
    
    def getHour(self):
        return self.time.hour
    
    def getMini(self):
        return self.time.minute
    
    def getSec(self):
        return self.time.second
    
    
    def __getNormalizeTime__(self):
        theTime = (self.getHour()) * 60 + self.getMini()
        return theTime
    
    def __unicode__(self):
        return self.getWeekday().toAbrevStr() + " " + str(self.time)
    
    def __str__(self):
        arr = str(self.time).split(':')
        timeStamp = arr[0] +':'+arr[1]
        return self.getWeekday().toAbrevStr() + " " + timeStamp
    
    #Rich Comparison
    def __eq__(self, other):
        if(other != None and other.__class__ == self.__class__) :
            return self.time == other.time and self.dayIndex == other.dayIndex
        else:
            return False
    
    def __lt__(self, other):
        if(other != None and other.__class__ == self.__class__) :
            if(self.dayIndex == other.dayIndex):
                return (self.time < other.time)
            return (self.dayIndex - other.dayIndex < 0)
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