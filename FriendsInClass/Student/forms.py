'''
Created on Feb 20, 2012

@author: chiehwu
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Student.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        

class StudentCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            profile = UserProfile(user = user)
            profile.save()
        return profile

class FriendListSearchForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required = False)
    last_name = forms.CharField(max_length=30, required = False)
    email = forms.EmailField(max_length=30, required = False,)
