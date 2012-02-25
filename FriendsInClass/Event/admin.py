from django.contrib import admin
from Event.models import Class
from Event.EventToStudent.models import ClassToStudent

class ClassAdmin(admin.ModelAdmin):
    list_display = ('dept', 'num', 'sect')

class ClassToStudentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student')
     
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassToStudent, ClassToStudentAdmin)