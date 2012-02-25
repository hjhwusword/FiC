'''
Created on Feb 17, 2012

@author: Hunlan
'''
from django.db import models
from Event.EventInterface import EventInterface
#from Event.EventToStudent.models import EventToStudent
from Util import Utilities

#TODO finish event class
class Event(models.Model, EventInterface):
    #need to be lower case before pass in
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    tRangesID = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    @staticmethod
    def getInstance(nameX,tRangesX):
        Class.__checkParam(nameX, tRangesX)
        
        # check SLN or others??
        databaseList = Event.objects.filter(name=nameX)
        
        if(len(databaseList) == 1):
            return databaseList[0] 
        else:
            instance = Event(name=nameX, tRangesID=tRangesX.id)
            instance.save()
            return instance
        
        
    @staticmethod
    def __checkParam(name, tRanges):
        Utilities.checkInstanceString(name)
        #Utilities.checkInstanceString(description)
        # check tRanges later TODO
   
    # @override
    def addStudent(self,studentUserProfile):
        student = self.__returnContainsStudent(studentUserProfile)
        if(student==None):
            self.students.add(studentUserProfile)
            
        raise ValueError("Student already registered to " + self.toAbrev()) 
    
    # @override
    def removeStudent(self, studentUserProfile):
        self.students.remove(studentUserProfile)
    
    # @override
    def getAllStudents(self):
        return self.students.all()
        
    # @override
    def containStudent(self, studentUserProfile):
        return not (self.__returnContainsStudent(studentUserProfile) == None)
    
    def __returnContainsStudent(self, studentUserProfile):
        L = self.students.filter(id=studentUserProfile.id)
        return L[0] if len(L) == 1 else None
    

class Class(models.Model, EventInterface):
    title = models.CharField(max_length = 50)          # Software Engineering
    dept = models.CharField(max_length = 10)           # CSE
    num = models.IntegerField(max_length = 3)           # 403
    sect = models.CharField(max_length = 2)           # A, AA
    location = models.CharField(max_length = 10)
    tRangesID = models.IntegerField()                               # UNKNOWN

    def __unicode__(self):
        return self.dept + str(self.num) + " " + self.sect
        
    @staticmethod
    def getInstance(titleX, deptX, numX, sectX, tRangesX):
        Class.__checkParam(titleX, deptX, numX, sectX, tRangesX)
        
        # check SLN or others??
        databaseList = Class.objects.filter(dept=deptX, num=numX, sect = sectX)
        
        if(len(databaseList) == 1):
            return databaseList[0] 
        else:
            instance = Class(title=titleX, dept=deptX, num=numX, sect=sectX, tRangesID=tRangesX.id)
            instance.save()
            return instance
        
        
    @staticmethod
    def __checkParam(title, dept, num, sectX, tRanges, sln, description):
        Utilities.checkInstanceString(title)
        Utilities.checkInstanceString(dept)
        Utilities.checkRange(num, 100, 1000)
        Utilities.checkInstanceString(sectX)
        Utilities.checkInstanceString(description)
        # check tRanges later TODO
        Utilities.checkRange(sln, 0, 1000000)
        
    
    # @override
    def addStudent(self,studentUserProfile):
        student = self.__returnContainsStudent(studentUserProfile)
        if(student==None):
            self.students.add(studentUserProfile)
            
        raise ValueError("Student already registered to " + self.toAbrev())
        
        
        
    # @override
    def removeStudent(self, studentUserProfile):
        self.students.remove(studentUserProfile)
    
    # @override
    def getAllStudents(self):
        return self.students.all()
        
    # @override
    def containStudent(self, studentUserProfile):
        return not (self.__returnContainsStudent(studentUserProfile) == None)
        
    def toAbrev(self):
        return str(self.dept) + str(self.num)
        
    def __returnContainsStudent(self, studentUserProfile):
        L = self.students.filter(id=studentUserProfile.id)
        return L[0] if len(L) == 1 else None
        
