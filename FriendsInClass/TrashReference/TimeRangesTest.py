#'''
#Created on 2012-2-15
#
#@author: jimmy
#'''
#import unittest
#from Event.TimeRanges.models import TimeRanges
#from Event.Times.models import Time
#from Event.TimeRange.models import TimeRange
#from Event.EnumWeek import EnumWeekday
#
#class Test(unittest.TestCase):
#    
#    def testAddTime(self):
#        timeRanges = TimeRanges
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        tr1 = TimeRange(time1,90)
#        timeRanges.addTime(tr1)
#        self.assertEqual(time1 in timeRanges.myTimeRange, True, "Test whether the add method is right")
#
#    def testRmoveTime(self):
#        timeRanges = TimeRanges
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        tr1 = TimeRange(time1,90)
#        timeRanges.addTime(tr1)
#        timeRanges.removeTime(tr1)
#        self.assertEqual(time1 in timeRanges.myTimeRange, False, "Test whether the remove method is right")
#        
#    def testCheckConflict(self):
#        timeRanges = TimeRanges
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        tr1 = TimeRange(time1,90)
#        time1 = Time(1,30,False, EnumWeekday.MONDAY)
#        tr2 = TimeRange(time1,90)
#        self.assertEqual(timeRanges.__checkConflict__(tr1,tr2), True, "Test whether the check conflict method is right")
