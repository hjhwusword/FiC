'''
Created on Feb 17, 2012

@author: Hunlan
'''
# hack from http://stackoverflow.com/questions/5983100/importerror-cannot-import-name-signals
from django.core import management;
import settings as settings
management.setup_environ(settings)

import unittest
from Event.Times.models import Time
from Event.EnumWeek import EnumWeekday
import datetime




class Test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        Time.removeAll()

    def testConstructorNormalCase(self):
        mon = EnumWeekday.MONDAY
        hour = 12
        mini = 30
        t = Time.getInstance(mon, hour, mini)

        self.assertEqual(mon, t.getWeekday(), "Weekday: Expect " + str(mon) + " but receive " + str(t.getWeekday()))
        self.assertEqual(hour, t.getHour(), "Hour: Expect " + str(hour) + " but receive " + str(t.getHour()))
        self.assertEqual(mini, t.getMini(), "Miniute: Expect " + str(mini) + " but receive " + str(t.getMini()))

    def testDataBaseHasElement(self):
        mon = EnumWeekday.MONDAY
        hour = 12
        mini = 30
        myTime = datetime.time(12,30)
        
        # no object in database
        L = Time.objects.filter(time=myTime, dayIndex=mon())
        # add object in database
        t = Time.getInstance(mon, hour, mini)
        self.assertTrue(1 == len(L), myMsg("Test Time Exist in Database", '1', str(len(L))))
    
    def testDataBaseNoRepeat(self):
        mon = EnumWeekday.MONDAY
        myTime = datetime.time(12,30)
        
        # no object in database
        L = Time.objects.filter(time=myTime, dayIndex=mon())
        # add object in database
        t = makeMon1230()
        # add object in database
        t = makeMon1230()
        self.assertTrue(1 == len(L), myMsg("Test No Repeat", '1', str(len(L))))
    
    def testShiftMon1230by30min(self):
        t1230 = makeMon1230()
        t1300_shifted = t1230.shift(30)
        t1300_real = Time.getInstance(EnumWeekday.MONDAY,13,00)
        self.assertEqual(t1300_real, t1300_shifted, myMsg("test shift", str(t1300_real), str(t1300_shifted))) 
        
    def testShiftMon2330by30min(self):
        t2330 = Time.getInstance(EnumWeekday.MONDAY, 23, 30)
        tShift = t2330.shift(30)
        tReal = Time.getInstance(EnumWeekday.TUESDAY, 00, 00)
        self.assertEqual(tReal, tShift, myMsg("test next day shift", str(tReal), str(tShift)))
    
    def testShiftSUN2330by60min(self):
        t2330 = Time.getInstance(EnumWeekday.SUNDAY, 23, 30)
        tShift = t2330.shift(60)
        tReal = Time.getInstance(EnumWeekday.MONDAY, 00, 30)
        self.assertEqual(tReal, tShift, myMsg("test sunday to monday shift", str(tReal), str(tShift)))

    def testMondayLessThanSunday(self):
        tmon = makeMon1230()
        tsun = Time.getInstance(EnumWeekday.SUNDAY, 12, 30)
        self.assertTrue(tmon < tsun, myMsg("test lt", "monday < sunday",  str(tmon<tsun)))

    def testSameDay1230MoreThan1200(self):
        t1 = makeMon1230()
        t2 = Time.getInstance(EnumWeekday.MONDAY, 12, 00)
        self.assertTrue(t1 > t2, myMsg("test same day compare", "12:30 > 12:00",  str(t1 > t2)))

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTimeModel']
    unittest.main()

def makeMon1230():
    mon = EnumWeekday.MONDAY
    hour = 12
    mini = 30
    myTime = datetime.time(12,30)
    return Time.getInstance(mon, hour, mini)

def myMsg(title, expect, receive):
    return title + " - expect: " + expect + "\treceive: " + receive
