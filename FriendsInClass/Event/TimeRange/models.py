'''
Created on Feb 18, 2012

@author: Hunlan
'''

from django.db import models
from Event.Times.models import Time

class TimeRange(models.Model):
#    timeID = models.IntegerField()
#    duration = models.IntegerField()
    startTime = models.ForeignKey(Time, related_name = 'startTime')
    endTime = models.ForeignKey(Time, related_name = 'endTime')
    
    @staticmethod
    def getInstance(start, end):
        if(not isinstance(start, Time)) : raise TypeError('"' + str(start) + '" is not a Time')
        if(not isinstance(end, Time)) : raise TypeError('"' + str(end) + '" is not a Time')
        #TODO: check db filter option
        databaseList = TimeRange.objects.filter(startTime=start, endTime=end)
        if(len(databaseList) == 1):
            return databaseList[0]
        else:
            instance = TimeRange(startTime=start, endTime=end)
            instance.save()
            return instance
        """   # check instance of variable
        # ClassSpecificUtilities.checkInstanceTime(time)
        if(not isinstance(time, Time)) : raise TypeError('"' + str(time) + '" is not a Time')
        Utilities.checkInstancePosInt(durationX)
        
        # get or create, but saving?        
        databaseList = TimeRange.objects.filter(timeID=time.id, duration=durationX)
        if(len(databaseList) == 1):
            return databaseList[0]
        else:
            instance = TimeRange(timeID=time.id, duration=durationX)
            instance.save()
            return instance
        """
        
    @staticmethod
    def removeAll():
        databaseList = TimeRange.objects.all()
        for tr in databaseList:
            tr.delete()
    
#    def getDuration(self):
#        return self.duration
    
    def getStartTime(self):
        return self.startTime
#        return Time.objects.get(id=self.timeID)
    
    def getEndTime(self):
        return self.endTime
#        myTime = Time.objects.get(id=self.timeID)
#        return myTime.shift(self.duration)
    
    def __eq__(self, other):
        if(other != None and other.__class__ == self.__class__) :
            return self.startTime == other.startTime and self.endTime == other.endTime
#            return self.timeID == other.timeID and self.duration == other.duration
        else:
            return False
        
    def __str__(self):
        
#        time = Time.objects.filter(id=self.timeID)
        return "Start: " + str(self.startTime) + "\tEnd: " + str(self.endTime)