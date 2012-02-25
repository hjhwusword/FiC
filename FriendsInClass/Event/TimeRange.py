#'''
#Created on Feb 10, 2012
#
#@author: Tony
#'''
#
#class TimeRange(object):
#    '''
#    classdocs
#    '''
#
#
#    def __init__(self, time, duration):
#        '''
#        Constructor
#        '''
#        # check instance of     
#        self.time = time
#        self.duration = duration
#        
#    def getEndTime(self):
#        self.end.hour = self.duration.hour + self.time.hour
#        self.end.min = self.duration.min + self.time.min
#        self.end.isPM = self.time.isPM
#        if self.end.min > 59:
#            self.end.min = self.end.min - 60
#            self.end.hour += 1
#        if self.end.hour >= 12:
#            self.end.isPM = not self.end.isPM
#            if not self.end.hour == 12:
#                self.end.hour -=12
#        return self.end
#    
#        
#    # TODO: not clear what this function is for
#    def __getNormalizeTime__(self):
#        theTime = 720 if self.isPM() else 0
#        theTime += (self.hour % 12) * 60 + self.min
#        return theTime
#        
#    def __equal__(self, other):
#        equal = True
#        if not self.time == other.time: equal = False
#        if not self.duration == other.duration: equal = False
#        return equal
#    
#    # TODO: function not clear
#    def __str__(self):
#        return None    
