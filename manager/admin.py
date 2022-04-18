from django.contrib import admin
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Project, Employee, Client


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many \
              and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


def projectsummary_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('admin_projectsummary_pdf', args=[obj.id])))

#    url = reverse('manager.admin_projectsummary_pdf', args=[obj.id])
#    return mark_safe(f'<a href="{url}">PDF</a>')


projectsummary_pdf.short_description = 'ProjectSummary'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'start_date', 'end_date', 'client_name',
                    'SOW_no', 'total_headcount', 'manager', projectsummary_pdf]
    list_filter = ['project_name', 'client_name', 'manager']
    list_editable = ['manager', 'client_name', 'start_date', 'end_date']
    actions = [export_to_csv]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'first_name', 'last_name', 'Email', 'DOJ',
                    'Project_manager', 'Location', 'Designation']
    list_filter = ['employee_name', 'Location', 'Project_manager', 'Designation']
    list_editable = ['Email', 'Location']
    actions = [export_to_csv]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'POC_client', 'POC_manager']
    list_filter = ['client_name', 'POC_client', 'POC_manager']
    list_editable = ['POC_client', 'POC_manager']
    actions = [export_to_csv]
