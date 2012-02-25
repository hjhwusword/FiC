'''
Created on Feb 18, 2012

@author: Hunlan
'''
from django.core import management;
import settings as settings
management.setup_environ(settings)

import unittest
from Event.Times.models import Time
from Event.TimeRange.models import TimeRange
from Event.EnumWeek import EnumWeekday

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        TimeRange.removeAll()
        Time.removeAll()

    # sanity check with database
    def testGetInstanceInDatabaseMon1030Duration50(self):
        t = getTime(1,10,30) # monday 10 30
        durationX = 50
        TimeRange.getInstance(t, durationX)
        L = TimeRange.objects.filter(timeID=t.id, duration=durationX)
        self.assertTrue(len(L) == 1, myMsg("database existance test", "exist", str(len(L) == 1)))

    # sanity check with getEndTime
    def testGetEndTime(self):
        t = getTime(1,10,30)
        durationX = 50
        tr = TimeRange.getInstance(t, durationX)
        tend = getTime(1,11,20)
        self.assertEqual(tend, tr.getEndTime(), myMsg("testing get end time", str(tend), str(tr.getEndTime())))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
def getTime(dayNum, hour, min):
    return Time.getInstance(EnumWeekday.fromInt(dayNum), hour, min)

def myMsg(title, expect, receive):
    return title + " - expect: " + expect + "\treceive: " + receive