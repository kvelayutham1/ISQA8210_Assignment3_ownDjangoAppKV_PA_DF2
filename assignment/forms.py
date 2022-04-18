from django import forms
from django.forms import ModelForm, DateInput
from .models import Assignment


class DateInput(DateInput):
    input_type = 'date'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('employee_name', 'allocation_percentage', 'Project_manager', 'start_date', 'end_date', 'email',
                  'project_name', 'comments')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
