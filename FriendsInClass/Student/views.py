#code review please

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect, get_object_or_404

from Student.models import UserProfile, YEAR_MAPPING, FriendList
from Student.forms import UserProfileForm, UserForm, StudentCreationForm, FriendListSearchForm

from Event.models import Event, Class
from Event.EventToStudent.models import ClassToStudent, EventToStudent

def createUser(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # The forms submitted by the client.
        creation_form = StudentCreationForm(request.POST)
        if creation_form.is_valid():
            # The forms validated correctly.
            creation_form.save()
            return redirect('/accounts/login/')
        else:
            return render_to_response('registration/create_user.html',
                                  {'creation_form': creation_form},
                                  context_instance = RequestContext(request))
    else:
        # Initialise the forms.
        creation_form = StudentCreationForm()
        return render_to_response('registration/create_user.html',
                                  {'creation_form': creation_form},
                                  context_instance = RequestContext(request))


@login_required(login_url='/accounts/login/')
def showSchedule(request):
    classes = ClassToStudent.objects.filter(student__id__exact = request.user.id)
    events = EventToStudent.objects.filter(student__id__exact = request.user.id)
    hasContents = len(classes) != 0 or len(events) != 0
    t = get_template('schedule/show_sche.html')
    html = t.render(Context({'classes' : classes, 'events' : events, 'hasContents' : hasContents}))
    return HttpResponse(html)

@login_required(login_url='/accounts/login/')
def showProfile(request):
    try:
        profile = UserProfile.objects.get(user__id__exact = request.user.id)
        if profile.year not in YEAR_MAPPING:
            profile.year = 'None'
        else :
            profile.year = YEAR_MAPPING[profile.year]
        t = get_template('user_profile.html')
        html = t.render(Context({'profile' : profile}))
        return HttpResponse(html)
    except UserProfile.DoesNotExist:
        raise Http404

@login_required(login_url='/accounts/login/')
def showFriend(request):
    try:
        friend = FriendList.objects.get(user__id__exact = request.user.id)
        t = get_template('show_friend.html')
        html = t.render(Context({'friend' : friend}))
        return HttpResponse(html)
    except UserProfile.DoesNotExist:
        raise Http404

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # The forms submitted by the client.
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            # The forms validated correctly.
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        # Initialise the forms.
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
        return render_to_response('edit_user_profile.html',
                                  {'user_form': user_form, 
                                   'profile_form': profile_form},
                                  context_instance = RequestContext(request))

@login_required(login_url='/accounts/login/')
def search_friend(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        friend_search_form = FriendListSearchForm(request.POST)
        ret = set()
        no_match = False
        if (friend_search_form.is_valid()):
            username = friend_search_form.cleaned_data['username']
            last_name = friend_search_form.cleaned_data['last_name']
            first_name = friend_search_form.cleaned_data['first_name']
            email = friend_search_form.cleaned_data['email']
            if (username):
                users = User.objects.filter(username = username)
                if (users):
                    ret = ret.union(set(users))
            if (last_name and first_name):
                users = User.objects.filter(last_name = last_name).filter(first_name = first_name)
                if (users):
                    ret = ret.union(set(users))
            elif (last_name):
                users = User.objects.filter(last_name = last_name)
                if (users):
                    ret = ret.union(set(users))
            elif (first_name):
                users = User.objects.filter(first_name = first_name)
                if (users):
                    ret = ret.union(set(users))
            if (email):
                users = User.objects.filter(email = email)
                if (users):
                    ret = ret.union(set(users))
            ret = __remove_duplicates(ret, request.user)
            no_match = len(ret) == 0
        return render_to_response('search_form.html',
                              {'friend_search_form': friend_search_form,
                               'result' : ret,
                               'no_match' : no_match},
                              context_instance = RequestContext(request))
    else :
        friend_search_form = FriendListSearchForm()
        return render_to_response('search_form.html',
                                  {'friend_search_form': friend_search_form},
                                  context_instance = RequestContext(request))
    
@login_required(login_url='/accounts/login/')
def add_friends(request):
    new_friends_list = request.POST.getlist('id')
    new_friends = set()
    for new_friend_id in new_friends_list:
        new_friends.add(get_object_or_404(User, id = new_friend_id))
    new_friends = __remove_duplicates(new_friends, request.user)
    for new_friend in new_friends:
        fl = FriendList(user=request.user, friend=new_friend)
        fl.save()
    return render_to_response('add_friends_done.html',
                              {'added_friends': new_friends},
                              context_instance = RequestContext(request))

@login_required(login_url='/accounts/login/')
def show_friends(request):
    relations = FriendList.objects.filter(user__id__exact = request.user.id)
    return render_to_response('friends.html',
                              {'relations': relations},
                              context_instance = RequestContext(request))

# remove friends that already have been followed from the given list
def __remove_duplicates(new_friends, user):
    old_friends = set()
    old_friends.add(user)
    user_friendlist = FriendList.objects.filter(user__id__exact = user.id)
    for relation in user_friendlist:
        old_friends.add(relation.friend)
    return new_friends - old_friends

def addEventToSchedule(request):
    event_id_list = request.POST.getlist('event_id')
    new_events = set()
    # add selected events into set
    for event_id in event_id_list:
        event = get_object_or_404(Event, id = event_id)
        new_events.add(event)
    # remove events already in the schedule
    old_events_list = Event.objects.filter(student__id__exact = request.user.id)
    old_events = set()
    for event in old_events_list:
        old_events.add(event)
    new_events = new_events - old_events
    for event in new_events:
        EventToStudent(event = event, student = request.user)
    # after add the event, show the schedule
    return render_to_response('add_event_done.html',
                              {'added_event': new_events},
                              context_instance = RequestContext(request))
    

def removeEventFromSchedule(request):
    event_id_list = request.POST.getlist('event_id')
    new_events = set()
    # add selected events into set
    for event_id in event_id_list:
        event = get_object_or_404(Event, id = event_id)
        new_events.add(event)
    for event in new_events:
        sch = EventToStudent.removeStudentFromEvent(student = request.user, event = event)
    # after add the event, show the schedule
    return render_to_response('remove_event_done.html',
                              {'removed_event': new_events},
                              context_instance = RequestContext(request))

def addClassToSchedule(request):
    class_id_list = request.POST.getlist('class_id')
    new_classes = set()
    # add selected events into set
    for class_id in class_id_list:
        course = get_object_or_404(Class, id = class_id)
        new_classes.add(course)
    # remove events already in the schedule
    old_classes_list = Class.objects.filter(student__id__exact = request.user.id)
    old_classes = set()
    for course in old_classes_list:
        old_classes.add(course)
    new_classes = new_classes - old_classes
    for course in new_classes:
        ClassToStudent(course = course, student = request.user)
    # after add the class, show the schedule   
    return render_to_response('add_class_done.html',
                              {'added_class': new_classes},
                              context_instance = RequestContext(request))
    

def removeClassFromSchedule(request):
    class_id_list = request.POST.getlist('class_id')
    new_classes = set()
    # add selected events into set
    for class_id in class_id_list:
        course = get_object_or_404(Class, id = class_id)
        new_classes.add(course)
    # remove events already in the schedule
    for course in new_classes:
        ClassToStudent.removeStudentFromClass(student = request.user,course = course)
    # after add the class, show the schedule   
    return render_to_response('remove_class_done.html',
                              {'removed_class': new_classes},
                              context_instance = RequestContext(request))