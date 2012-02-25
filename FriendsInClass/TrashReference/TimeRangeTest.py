#'''
#Created on 2012-2-15
#
#@author: jimmy
#'''
#import unittest
##import FriendsInClass.Event.EnumWeekday
#from Event.TimeRange import TimeRange
#from Event.Time import Time
#from Event.EnumWeek import EnumWeekday
#
#class Test(unittest.TestCase):
#    
#    def testConstrcutor(self):
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        timeRange1 = TimeRange(time1,90)
#        time2 = Time(1,10,False, EnumWeekday.MONDAY)
#        self.assertEqual(timeRange1.time.__eq__(time2), True, "Test whether the constructor set the parameter right")
#        self.assertEqual(timeRange1.time.duration, 90, "Test whether the constructor set the parameter right")
#        
#        
#        
#    def testGetEndTime(self):   
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        timeRange1 = TimeRange(time1,90)
#        self.assertEqual(timeRange1.getEndTime().__getNormalizeTime__(), 160, "1:10 am with 90 min duration should end at 160min")
#        
#    def testEqual(self):
#        time1 = Time(1,10,False, EnumWeekday.MONDAY)
#        timeRange1 = TimeRange(time1,90)
#        time2 = Time(1,30,False, EnumWeekday.MONDAY)
#        timeRange2 = TimeRange(time1,70)
#        self.assertEqual(timeRange1.__equal__(timeRange2),True, "Test whether the Equal method is right")
