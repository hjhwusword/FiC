'''
Created on Feb 18, 2012 (2:06AM)
Test Driven
@author: Hunlan
'''
#from django.core import management;
#import settings as settings
#management.setup_environ(settings)

import unittest
from Event.TimeRanges.models import TimeRanges
from Event.Times.models import Time
from Event.TimeRange.models import TimeRange
from Event.EnumWeek import EnumWeekday

class Test(unittest.TestCase):


    def setUp(self):
        TimeRanges.removeAll()
        TimeRange.removeAll()
        Time.removeAll()


    def tearDown(self):
        TimeRanges.removeAll()
        TimeRange.removeAll()
        Time.removeAll()


    def testConstructingExistInDatabase(self):
        trs = TimeRanges.getInstance()
        L = TimeRanges.objects.filter(id=trs.id)
        self.assertTrue(len(L) == 1, myMsg("test constructor", "existance", str(len(L)==1)))

    def testAdd1Time(self):
        tr = makeCSE403TimeRange()
        trs = TimeRanges.getInstance()
        trs.addTimeRange(tr)
        self.assertEqual(tr, trs.getAll()[0], myMsg("test add 1 time", str(tr), str(trs.getAll())[0]))
        
    def testAddConflictTimeThrowValueError(self):
        tr = makeCSE403TimeRange()
        trs = TimeRanges.getInstance()
        trs.addTimeRange(tr)
        self.failUnlessRaises(ValueError, trs.addTimeRange, tr)
        
    def testAddTimeEndAndStartAtTheSameTime(self):
        t2 = Time.getInstance(EnumWeekday.MONDAY, 9, 30)
        tr2 = TimeRange.getInstance(t2, 60)
        
        tr = makeCSE403TimeRange()
        
        trs = TimeRanges.getInstance()
        
        trs.addTimeRange(tr)
        trs.addTimeRange(tr2)
        
        #should not throw an error
    
    def testAddTimeAndRemoveIt(self):
        tr = makeCSE403TimeRange()
        trs = TimeRanges.getInstance()
        trs.addTimeRange(tr)
        trs.removeTimeRange(tr)
        self.assertTrue(trs.isEmpty(), "TimeRanges is not empty!")
    
    def testAdd1Add2Remove1And2Exist(self):
        tr = makeCSE403TimeRange()
        t2 = Time.getInstance(EnumWeekday.MONDAY, 9, 30)
        tr2 = TimeRange.getInstance(t2, 60)
        
        trs = TimeRanges.getInstance()
        trs.addTimeRange(tr)
        trs.addTimeRange(tr2)
        trs.removeTimeRange(tr)
        self.assertTrue(trs.containTime(tr2), "tr2 should be in trs but got removed")
        
    def testRemoveEmptyTimeRange(self):
        trs = TimeRanges.getInstance()
        trs.removeTimeRange(makeCSE403TimeRange())
        self.assertTrue(trs.isEmpty(), "Should be empty and no error thrown")
        
    def testDoNotContainAnyTime(self):
        trs = TimeRanges.getInstance()
        self.assertFalse(trs.containTime(makeCSE403TimeRange()), "Should not contain Mon10:30 50min")
    
    def testContainCSE403Time(self):
        trs = TimeRanges.getInstance()
        trs.addTimeRange(makeCSE403TimeRange())
        self.assertTrue(trs.containTime(makeCSE403TimeRange()), "Should contain MON10:30 50min")
        
    def testGetAll(self):
        tr = makeCSE403TimeRange()
        t2 = Time.getInstance(EnumWeekday.MONDAY, 9, 30)
        tr2 = TimeRange.getInstance(t2, 60)
        t3 = Time.getInstance(EnumWeekday.MONDAY, 8, 30)
        tr3 = TimeRange.getInstance(t3, 60)
        
        trs = TimeRanges.getInstance()
        trs.addTimeRange(tr)
        trs.addTimeRange(tr2)
        trs.addTimeRange(tr3)
        
        allTRs = trs.getAll()
        
        self.assertTrue(tr in allTRs, str(tr) + " not in trs when getall is called")
        self.assertTrue(tr2 in allTRs, str(tr2) + " not in trs when getall is called")
        self.assertTrue(tr3 in allTRs, str(tr3) + " not in trs when getall is called")
        
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
def myMsg(title, expect, receive):
    return title + " - expect: " + expect + "\treceive: " + receive


def makeCSE403TimeRange():
    t = Time.getInstance(EnumWeekday.MONDAY, 10, 30)
    return TimeRange.getInstance(t, 50) 



