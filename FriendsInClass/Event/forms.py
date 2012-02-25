'''
Created on 2012-2-22

@author: jimmy
'''


from django.forms import ModelForm
from Event.models import Event
from Event.models import Class

class EventForm(ModelForm):
    class Meta:
        model = Event

class ClassForm(ModelForm):
    class Meta:
        model = Class


