'''
Created on Feb 18, 2012

@author: Hunlan, Hans
'''

from django.db import models
from django.http import Http404
from django.contrib.auth.models import User
from Event.models import Class
from Event.models import Event

class EventToStudent(models.Model):
    event = models.ForeignKey(Event)
    student = models.ForeignKey(User)
    
    # @param param: student a User
    # @param param: event a Event 
    @staticmethod
    def addStudentToEvent(student, event):
        try:
            #check if both student and event are in database
            Event.objects.get(id__exact = event.id)
            User.objects.get(id__exact = student.id)
            
            #check if student already joined the event
            databaseList = EventToStudent.objects.filter(student__id__exact = student.id).filter(event__id_exact = event.id)
            if(len(databaseList) != 0):
                raise ValueError("Student " + str(student) + " already in " + str(event))
            instance = EventToStudent(event=event, student=student)
            instance.save()
        except Event.DoesNotExist:
            raise Http404
        except User.DoesNotExist:
            raise Http404
    
    # @param param: student a User
    # @param param: event a Event 
    @staticmethod
    def removeStudentFromEvent(student, event):
        try:
            #check if both student and event are in database
            Event.objects.get(id__exact = event.id)
            User.objects.get(id__exact = student.id)
            
            #check if student already joined the event
            databaseList = EventToStudent.objects.filter(student__id__exact = student.id)
            if(len(databaseList) == 0):
                raise ValueError("Student " + str(student) + " is not in " + str(event))
            databaseList[0].delete()
        except Event.DoesNotExist:
            raise Http404
        except User.DoesNotExist:
            raise Http404

class ClassToStudent(models.Model):
    course = models.ForeignKey(Class)
    student = models.ForeignKey(User)  

    @staticmethod
    def removeStudentFromClass(student, course):
        try:
            #check if both student and event are in database
            Class.objects.get(id__exact = course.id)
            User.objects.get(id__exact = student.id)
            
            #check if student already joined the event
            databaseList = ClassToStudent.objects.filter(student__id__exact = student.id)
            if(len(databaseList) == 0):
                raise ValueError("Student " + str(student) + " is not in " + str(course))
            databaseList[0].delete()
        except Event.DoesNotExist:
            raise Http404
        except User.DoesNotExist:
            raise Http404   