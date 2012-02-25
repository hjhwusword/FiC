'''
Created on Feb 18, 2012

@author: Hunlan & Jimmy

'''
from django.db import models
from Event.TimeRange.models import TimeRange

class TimeRanges(models.Model):
    # stub not going to be integer
    # timeRanges = models.IntegerField()
    timeRanges = models.ManyToManyField(TimeRange)


    
    @staticmethod
    def getInstance():
        '''nullTRs = TimeRanges.objects.filter(timeRanges=None)
        if(len(nullTRs) != 0) :
            return nullTRs[0]
        else:
            trs = TimeRanges()
            trs.save()
            return trs'''
        trs = TimeRanges()
        trs.save()
        return trs
    
    @staticmethod
    def removeAll():
        L = TimeRanges.objects.all()
        for trs in L :
            trs.delete()
    
    def addTimeRange(self, timeRange):
        if(self.__hasConflict(timeRange)):
            raise ValueError("Time Conflict")
        
        self.timeRanges.add(timeRange)
        
        '''self.timeRanges.add(timeRange)
        dbTRs = self.__recursiveFilter(self.timeRanges.all())
        if(len(dbTRs) != 0) :
            self = dbTRs[0]
        else:
            self.save()'''
    
    def removeTimeRange(self, timeRange):
        self.timeRanges.remove(timeRange)
    
    def containTime(self, tr):
        L = self.timeRanges.filter(id=tr.id)
        return len(L) == 1
    
    def isEmpty(self):
        return not self.timeRanges.exists()
    
    def getAll(self):
        # django book 2.0 chap 7
        return self.timeRanges.all()

    def __recursiveFilter(self, L):
        if(len(L) == 0) :
            return []
        if(len(L) == 1) :
            return TimeRanges.objects.filter(timeRanges=L[0].id)
        return TimeRanges.objects.filter(timeRanges=L[0].id) & self.__recursiveFilter(L[1:]) 
    
    
    def __hasConflict(self, tr):
        allTRs = self.timeRanges.all()
        for Tred in allTRs:
            if ((Tred.getStartTime() <= tr.getStartTime()) and 
                        (Tred.getEndTime() > tr.getStartTime())):
                return True
            
            if ((tr.getStartTime() <= Tred.getStartTime()) and
                        (tr.getEndTime() > Tred.getStartTime())):
                return True
                
        return False
    
    
    
    
    
    
    
    