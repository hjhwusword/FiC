from django.contrib import admin
from Student.models import UserProfile, FriendList

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'year')

class FriendListAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(FriendList, FriendListAdmin)