from django.contrib import admin
from api.models import *





class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created')
    search_fields = ('title',)
    list_filter = ('user',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'user', 'start_date', 'end_date')
    search_fields = ('institution', 'degree')
    list_filter = ('user',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'user', 'start_date', 'end_date')
    search_fields = ('job_title', 'company')
    list_filter = ('user',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    search_fields = ('name', 'email')

# Register your models here.


admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)