'''
Created on Feb 18, 2012

@author: liujh
'''
from django.utils import unittest
from django.test.client import Client

username = 'test'
password = 'test'

class TestSchedule(unittest.TestCase):
    def __login(self):
        c = Client()
        c.post('/accounts/login/', {'username': username, 'password': password})
        return c
    
    def testShowSchedule(self):
        c = self.__login()
        response = c.post('/schedule/')
        self.failUnlessEqual(response.status_code, 200)
        
    def testShowProfile(self):
        c = self.__login()
        response = c.post('/accounts/profile/')
        self.failUnlessEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()