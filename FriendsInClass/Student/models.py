from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

YEAR_MAPPING = {'FR' : 'Freshman',
                'SO' : 'Sophomore',
                'JR' : 'Junior',
                'SR' : 'Senior',
                'GR' : 'Graduate',
                }

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank = True, null = True)
    phone_num = PhoneNumberField(blank = True, null = True)
    
    def __unicode__(self):
        return self.user.username

class FriendList(models.Model):
    user = models.ForeignKey(User, related_name='user')
    friend = models.ForeignKey(User, related_name='friend')
    
    def __unicode__(self):
        return self.user.username + "'s Friend List"