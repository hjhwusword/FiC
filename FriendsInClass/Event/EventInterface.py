'''
Created on Feb 10, 2012

@author: Hunlan
'''
# this is an interface okay?
class EventInterface:
    
    def addStudent(self,student):
        return None
    
    def removeStudent(self, student):
        return None
    
    def getAllStudents(self):
        return None
    
    def containStudent(self, student):
        return False