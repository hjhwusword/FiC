'''import unittest
from Event.Time import Time
from Event.EnumWeek import EnumWeekday

class testTime(unittest.TestCase):
    def testConstructStartError(self): # NEED TO CHANGE THIS
        myTime = Time(1,10,True, EnumWeekday.MONDAY)
        print(myTime.__getNormalizeTime__())
        
    def testNormalizeTimeNormalCase(self):
        myTime = Time(4,30,False, EnumWeekday.FRIDAY)
        self.assertEqual(myTime.__getNormalizeTime__(), 270, "Test whether 4:30am converts to 270 min")
        
    def testNormalizeTimePMNormalCase(self):
        myTime = Time(4,40,True, EnumWeekday.FRIDAY)
        self.assertEqual(myTime.__getNormalizeTime__(), 1000, "Test whether 4:40pm converts to 1000 min")
        
    def testNormalizeTime1200pmCase(self):
        myTime = Time(12,00,True, EnumWeekday.FRIDAY)
        self.assertEqual(myTime.__getNormalizeTime__(), 720, "Test whether 12:00pm converts to 720 min")
        
    def testNormalizeTime1200amCase(self):
        myTime = Time(12,00,False, EnumWeekday.FRIDAY)
        self.assertEqual(myTime.__getNormalizeTime__(), 0, "Test whether 12:00am converts to 0 min")

    def testTimeEqual(self):
        t1 = Time(12,00,False,EnumWeekday.MONDAY)
        t2 = Time(12,00,False,EnumWeekday.MONDAY)
        self.assertTrue(t1 == t2, "Test if 2 times are the same")
    
    
    def testShiftNormal(self):
        myTime = Time(5,00,True, EnumWeekday.FRIDAY)
        self.assertEqual(myTime.shift(90), Time(6,30,True, EnumWeekday.FRIDAY), "Test whether 90 min after 5pm is 6:30pm")
        
    def testShiftDay(self):
        myTime = Time(11,00,True, EnumWeekday.FRIDAY)
        newTime = myTime.shift(90)
        realNewTime = Time(12,30,False, EnumWeekday.SATURDAY)
        self.assertEqual(newTime, realNewTime, str(newTime) + " is not the real " + str(realNewTime) )
        
    def testShiftAMPM(self):
        myTime = Time(11,59,False, EnumWeekday.FRIDAY)
        newTime = myTime.shift(1)
        realNewTime = Time(12,00,True, EnumWeekday.FRIDAY)
        self.assertEqual(newTime, realNewTime, str(newTime) + " is not the real " + str(realNewTime) )
        
    def testCompareDifferentDay(self):
        myT1 = Time(10,0,False, EnumWeekday.MONDAY)
        myT2 = Time(10,0,False, EnumWeekday.TUESDAY)
        self.assertTrue(myT1 < myT2, "myT1 < myT2 yeild value: " + str(myT1 < myT2))
        
    def testCompareDifferentTimeSameDay(self):
        myT1 = Time(10,0,False, EnumWeekday.MONDAY)
        myT2 = Time(10,1,False, EnumWeekday.MONDAY)
        self.assertTrue(myT1 < myT2, "myT1 < myT2 yeild value: " + str(myT1 < myT2))
        
        
        
        
        '''