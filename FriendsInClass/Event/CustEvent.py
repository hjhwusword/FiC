'''
Created on Feb 10, 2012

@author: Jimmy
'''

from Event.EventInterface import EventInterface

class CustEvent(EventInterface):
    '''
    classdocs
    '''


    def __init__(self, title, tRanges, id):
        '''
        Constructor
        '''
        self.title = title
        self.tRanges = tRanges
        self.id = id
        self.students = []
    
    #Override    
    def addStudent(self,student):
        self.students.append(student)
    
    #Override    
    def removeStudent(self, student):
        self.students.remove(student)
    
    #Override
    def getAllStudents(self):
        return self.students
    
    #Override
    def containStudent(self, student):
        return student in self.students
    
        