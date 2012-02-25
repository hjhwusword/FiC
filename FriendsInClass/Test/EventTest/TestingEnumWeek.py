'''
Created on Feb 10, 2012

@author: Hunlan
'''
import unittest
#import FriendsInClass.Event.EnumWeekday
from Event.EnumWeek import EnumWeekday

class Test(unittest.TestCase):
    def testCallableIntReturn(self):
        friday = EnumWeekday.FRIDAY
        self.assertEqual(friday(), 5, "testing if friday has index 5")
        
    def testToStringMethod(self):
        tuesday = EnumWeekday.TUESDAY
        self.assertEqual(str(tuesday), "Tuesday", \
                         'testing if tuesday has string Tuesday')

    def testToAbrevMethod(self):
        monday = EnumWeekday.MONDAY
        self.assertEqual(monday.toAbrevStr(), "MON", \
                         'testing if Monday has abrev string MON')
    
    def testNextDayMethodWednesday(self):
        wed = EnumWeekday.WEDNESDAY
        self.assertEqual(wed.nextDay(), EnumWeekday.THURSDAY, \
                         "Test if wednes's next day is Thurs")
        
    def testNextDayMethodSunday(self):
        sunday = EnumWeekday.SUNDAY
        self.assertEqual(sunday.nextDay(), EnumWeekday.MONDAY, \
                         "Test if Sunday's next day is Monday")
        
    def testNextDayIsImmutableReturn(self):
        monday = EnumWeekday.MONDAY
        monday.nextDay()
        self.assertEqual(monday, EnumWeekday.MONDAY, \
                         "Test if perform next day will not change the previous")

    def testNotEqualsNormal(self):
        self.assertNotEqual(EnumWeekday.MONDAY, 1, "Test whether equals will fail if different class object")
        
    def testNotEqualsDiffernetDau(self):
        self.assertNotEqual(EnumWeekday.MONDAY, EnumWeekday.THURSDAY, "Test whether equals will fail if day")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()