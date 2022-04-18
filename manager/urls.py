"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path, re_path

urlpatterns = [
#    path('', views.home, name='home'),
#    re_path(r'^home/$', views.home, name='home'),
    path('project_list/', views.project_list, name='project_list'),
    path('project_list/admin_projectlist_pdf/', views.admin_projectlist_pdf, name='admin_projectlist_pdf'),
    path('project/create/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:pk>/project_summary/', views.project_summary, name='project_summary'),
    path('admin/project/<int:pk>/pdf/',
         views.admin_projectsummary_pdf,
         name='admin_projectsummary_pdf'),
    path('project/<int:pk>/project_summary/pdf/',
         views.admin_projectsummary_pdf1,
         name='admin_projectsummary_pdf1'),
    path('client_list/', views.client_list, name='client_list'),
    path('client_list/clientlist_pdf', views.clientlist_pdf, name='clientlist_pdf'),
    path('client/create/', views.client_new, name='client_new'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_list/employeelist_pdf', views.employeelist_pdf, name='employeelist_pdf'),
    path('employee/create/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employee/<int:pk>/employee_assignment/', views.employee_assignment, name='employee_assignment'),
]
