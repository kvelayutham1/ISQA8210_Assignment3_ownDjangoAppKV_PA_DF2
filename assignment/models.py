from datetime import timezone, date
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from manager.models import Client, Project, Employee

# from users.models import Customuser
# Create your models here.
import users.models


class Assignment(models.Model):
    employee_name = models.ForeignKey(Employee, related_name='name', blank=False, null=False, default=' ',
                                      on_delete=models.CASCADE)
    #    client_id = models.CharField(max_length=50, blank=False, null=False, default=' ')
    allocation_percentage = models.IntegerField(blank=False, null=False, default=' ')
    Project_manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateField(default=' ')
    end_date = models.DateField(default=' ')
    email = models.EmailField(max_length=100, default='example@gmail.com')
    project_name = models.ForeignKey(Project, related_name='client', max_length=50, blank=False,
                                     null=False, default=' ',
                                     on_delete=models.CASCADE)
    comments = models.CharField(max_length=50, blank=False, null=False, default=' ')

    def __int__(self):
        return self.employee_name

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])


