from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'department', 'date_of_joining', 'employee_ID',
                  'office_location', 'cell_phone', 'designation')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'department', 'date_of_joining', 'employee_ID',
                  'office_location', 'cell_phone', 'designation')
