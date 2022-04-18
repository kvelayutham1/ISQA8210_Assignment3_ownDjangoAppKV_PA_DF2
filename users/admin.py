from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import csv
import datetime
from django.http import HttpResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

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

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'department', 'cell_phone', 'is_staff', 'date_of_joining', 'employee_ID',
                    'first_name', 'last_name',]


admin.site.register(CustomUser, CustomUserAdmin)
