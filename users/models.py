from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')
    date_of_joining = models.DateField(null=True, blank=True)
    employee_ID = models.CharField(max_length=50, default=' ', null=True, blank=True)
    office_location = models.CharField(max_length=50, default=' ', null=True, blank=True)
    designation = models.CharField(max_length=50, default=' ', null=True, blank=True)
