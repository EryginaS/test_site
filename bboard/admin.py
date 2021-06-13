from django.contrib import admin
from django.db.models.query_utils import Q

from .models import Applications, Clients, Dept, ItPerson, Report
from django.urls import get_urlconf, get_resolver
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.db import models
from django.shortcuts import render, redirect
import io
from django.http import HttpResponse
from django.urls import reverse
from .forms import ReportForm
from .helpers import doc_render_for_report
from wsgiref.util import FileWrapper

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('__str__','theme', 'type_app', 'priority', 'status', 'responsible', )
    list_display_links = ('__str__',)
    fields = ('theme', 'type_app', 'priority', 'status', 'responsible', 'desc', 'client', 'date')
    list_editable = ( 'status', 'responsible')
    readonly_fields = ('client', )
    actions = ['make_report']
    def make_report(self, request, queryset):
        if queryset:
            if queryset.count() > 1:
                return 
            else:
                q = queryset[0]
                try:
                    report = Report.objects.get(application=q)
                    return redirect(reverse("admin:bboard_report_change", args=(report.id,)))
                except Report.DoesNotExist:

                    report = Report(application=q, theme=q.theme, desc=q.desc,\
                        client=q.client, date=q.date, responsible=q.responsible,\
                            priority=q.priority, status=q.status, type_app=q.type_app,\
                                )
                    report.report_maker = request.user
                    report.save()
                    return redirect(reverse("admin:bboard_report_change", args=(report.id,)))
                   
    make_report.short_description = "Cформировать отчет"

class ReportAdmin(admin.ModelAdmin):
    list_display = ('__str__','theme', 'type_app', 'priority', 'status', 'responsible', 'done_work', 'application', 'report_maker')
    list_display_links = ('__str__',)
    fields = ('theme', 'type_app', 'priority', 'status', 'responsible', 'desc', 'client', 'date', 'done_work', 'application', 'report_maker')
    list_editable = ( 'status', 'responsible')
    readonly_fields = ('client', 'application', 'report_maker')
    actions = ['make_report_in_word']
    
    def make_report_in_word(self, request, queryset):
        if queryset:
            if queryset.count() > 1:
                    return 
            else:
                q = queryset[0]
                doc = doc_render_for_report(q)
                doc_io = io.BytesIO() # create a file-like object
                doc.save(doc_io) # save data to file-like object
                doc_io.seek(0) # go to the beginning of the file-like object

                response = HttpResponse(doc_io.read())
                response["Content-Disposition"] = f"attachment; filename=report_{q.application.pk}.docx"
                response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

                return response

            pass
    
    make_report_in_word.short_description = "Оформить и выгрузить отчет"

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
admin.site.register(Report, ReportAdmin)

