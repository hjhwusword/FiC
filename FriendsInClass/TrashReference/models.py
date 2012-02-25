''' Depricated
Created on Feb 14, 2012

@author: Hunlan
'''
'''from django.db import models
from Util import Utilities

class ClassStudentTable(models.Model):
    classSLN = models.IntegerField()
    studentTag = models.IntegerField()
    
    def __unicode__(self):
        return u'SLN:%s-->ID:%s' % (self.classSLN, self.studentTag)

    @staticmethod
    def initSave(theSLN, theTag):
        instance = ClassStudentTable(classSLN=theSLN,studentTag=theTag)
        instance.save()
        return instance

    @staticmethod
    def getStudentList(theClassSLN):
        Utilities.checkInstancePosInt(theClassSLN)
        return ClassStudentTable.objects.filter(classSLN=theClassSLN)
        
    @staticmethod
    def removeAll():
        L = ClassStudentTable.objects.all()
        for theClassSLN in L :
            theClassSLN.delete()'''