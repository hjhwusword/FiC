#'''
#Created on Feb 10, 2012
#
#@author: Jimmy
#'''
#
#
#class MyClass(object):
#    '''
#    classdocs
#    '''
#
#
#    def __init__(self):
#        '''
#        Constructor
#        '''
#        self.myTimeRange = []
#        
#    def addTime(self, time):
#        self.myTimeRange.append(time)
#    
#    def removeTime(self, time):
#        self.myTimeRange.remove(time)
#    
#    def containTime(self, time):
#        return time in self.myTimeRange
#    
#        
#    def __checkConflict__(self, tr1, tr2):
#        mask = tr1.getEndTime().__gt__(tr2.time) or tr2.getEndTime().__gt__(tr1.time)