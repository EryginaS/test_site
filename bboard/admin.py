from django.contrib import admin

from .models import Applications, Clients, Dept, ItPerson
from django.urls import get_urlconf, get_resolver
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.db import models


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('__str__','theme', 'type_app', 'priority', 'status', 'responsible', )
    list_display_links = ('__str__',)
    fields = ('theme', 'type_app', 'priority', 'status', 'responsible', 'desc', 'client', 'date')
    list_editable = ( 'status', 'responsible')
    readonly_fields = ('client', )


class ItPersonAdmin(admin.ModelAdmin):
    list_display = ('__str__','user', 'phone')
    list_display_links = ('__str__',)
    
    list_editable = ( 'phone',)
    

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('__str__','user', 'dept', 'phone', 'email')
    list_display_links = ('__str__',)
    
    list_editable = ( 'phone', 'dept', 'email')
    


class DeptAdmin(admin.ModelAdmin):
    list_display = ('__str__','name', 'main_person', 'desc')
    list_display_links = ('__str__',)
    
    list_editable = ( 'desc',)
    
    

admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(ItPerson, ItPersonAdmin)
admin.site.register(Dept, DeptAdmin)

