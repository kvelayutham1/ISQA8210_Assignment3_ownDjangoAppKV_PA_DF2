from django import forms
from .models import Project, Client, Employee
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, DateInput


class DateInput(DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'start_date', 'end_date', 'client_name', 'SOW_no',
                  'total_headcount', 'manager')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'POC_client', 'POC_manager')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name', 'first_name', 'last_name', 'Email', 'DOJ', 'Project_manager', 'Location',
                  'Designation')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'DOJ': DateInput(),
        }
