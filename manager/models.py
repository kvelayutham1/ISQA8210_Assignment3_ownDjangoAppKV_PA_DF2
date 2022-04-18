from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
import users.models


class Client(models.Model):
    client_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
#    client_id = models.CharField(max_length=50, blank=False, null=False, default=' ')
    POC_client = models.CharField(max_length=50, blank=False, null=False, default=' ')
    POC_manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
#    project_ID = models.CharField(max_length=50, blank=False, null=False, default=' ')
    project_description = models.CharField(max_length=50, blank=False, null=False, default=' ')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    client_name = models.ForeignKey(Client, related_name='client', max_length=50, blank=False, null=False, default=' ',
                                    on_delete=models.CASCADE)
    SOW_no = models.CharField(max_length=50, blank=False, null=False, default=' ')
    total_headcount = models.IntegerField(blank=False, null=False, default=' ')
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

#    def get_absolute_url(self):
#        return reverse('home', args=[str(self.id)])


class Employee(models.Model):
    employee_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
#    employee_ID = models.CharField(max_length=50, blank=False, null=False, default=' ')
    first_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    last_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    Email = models.EmailField(max_length=100, default=' ')
    DOJ = models.DateField(null=True, blank=True)
    Project_manager = models.ForeignKey(users.models.CustomUser, related_name='manager', null=True,
                                        on_delete=models.DO_NOTHING)
    Location = models.CharField(max_length=50, blank=False, null=False, default=' ')
    Designation = models.CharField(max_length=50, blank=False, null=False, default=' ')

    def __str__(self):
        return self.employee_name

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
