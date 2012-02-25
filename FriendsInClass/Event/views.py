'''
Created on 2012-2-24

@author: jimmy
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from Event.forms import EventForm

@login_required(login_url='/accounts/login/')
def createEvent(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # The forms submitted by the client.
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
        return render_to_response('event/createEvent_success.html',
                                  {'event_form': event_form},
                                  context_instance = RequestContext(request))
    else:
        # Initialise the forms.
        event_form = EventForm()
        return render_to_response('event/createEvent.html',
                                  {'event_form': event_form},
                                  context_instance = RequestContext(request))

@login_required(login_url='/accounts/login/')
def searchEvent(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # The forms submitted by the client.
        pass
    else:
        # Initialise the forms.
        pass

@login_required(login_url='/accounts/login/')
def searchClass(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # The forms submitted by the client.
        pass
    else:
        # Initialise the forms.
        pass