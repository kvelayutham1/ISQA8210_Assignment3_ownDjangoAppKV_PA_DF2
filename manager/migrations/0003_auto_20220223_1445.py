# Generated by Django 3.2.8 on 2022-02-23 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0002_remove_employee_assigned_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client_id',
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default=' ', max_length=50)),
                ('client_id', models.CharField(default=' ', max_length=50)),
                ('POC_client', models.CharField(default=' ', max_length=50)),
                ('POC_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
