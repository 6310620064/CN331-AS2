from django.contrib import admin

from .models import Register, Subject

#buid table in database
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'subject_name' ,'semester' , 'academic_year' , 'quota' ,'student', 'status']
    list_filter = ['status']
    search_fields = ['code' , 'subject_name']

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user' , 'subject']
    #subjects from def Student

#Register your models here.
admin.site.register(Register , RegisterAdmin)
admin.site.register(Subject, SubjectAdmin)

