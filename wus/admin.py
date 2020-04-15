from django.contrib import admin
from .models import Project
from django.contrib.auth.models import Group

admin.site.site_header = 'BentleyCAE Site Dashboad'



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'proj_date')

admin.site.register(Project,ProjectAdmin)




admin.site.unregister(Group)
