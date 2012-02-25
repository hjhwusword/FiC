from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done
from django.contrib import admin
from Student.views import showSchedule, showProfile, edit_profile, createUser, search_friend, add_friends, show_friends
from Event.views import createEvent

admin.autodiscover()

'''This is the place for you to put html pages'''
urlpatterns = patterns('',
    (r'^$', showProfile),                   
    
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # registration
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout_then_login, {'login_url' : '/accounts/login'}),
    (r'^accounts/password_change/$', password_change, {'post_change_redirect' : '/accounts/change_password/done/'}),
    (r'^accounts/change_password/done/$', password_change_done),
    (r'^accounts/profile/$', showProfile),
    (r'^accounts/register/$', createUser),
    
    # Profile
    (r'^profile/$', edit_profile),
    (r'^schedule/$', showSchedule),
    
    # event
    (r'^event/create/$', createEvent),
    
    (r'^friends/search/$', search_friend),
    (r'^friends/add/$', add_friends),
    (r'^friends/show/$', show_friends),
)
