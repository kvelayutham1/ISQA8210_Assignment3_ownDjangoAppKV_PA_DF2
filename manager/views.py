from django.shortcuts import render, redirect

from users.models import CustomUser
from .models import *
from .forms import *
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from assignment.models import Assignment
from django.conf import settings
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import weasyprint
from io import BytesIO
from django.core.mail import send_mail

# Create your views here.

now = timezone.now()


def home(request):
    return render(request, 'home.html', {'manager': home})


@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_date = timezone.now()
            project.save()
            projects = Project.objects.all
            return render(request, 'project_list.html',
                          {'projects': projects})
    else:
        form = ProjectForm()
        # print("Else")
    return render(request, 'project_new.html', {'form': form})


@login_required
def project_list(request):
    #    project = Project.objects.filter(created_date__lte=timezone.now())
    project = Project.objects.all()
    return render(request, 'project_list.html',
                  {'projects': project})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        # update
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.updated_date = timezone.now()
            project.save()
            #            project = Project.objects.filter(created_date__lte=timezone.now())
            project = Project.objects.all()
            return render(request, 'project_list.html',
                          {'projects': project})
    else:
        # edit
        form = ProjectForm(instance=project)
    return render(request, 'project_edit.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')


# Clients
@login_required
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_date = timezone.now()
            client.save()
            clients = Client.objects.all
            return render(request, 'client_list.html',
                          {'clients': clients})
    else:
        form = ClientForm()
        # print("Else")
    return render(request, 'client_new.html', {'form': form})


@login_required
def client_list(request):
    #    project = Project.objects.filter(created_date__lte=timezone.now())
    client = Client.objects.all()
    return render(request, 'client_list.html',
                  {'clients': client})


@login_required
def clientlist_pdf(request):
    client = Client.objects.all()
    html = render_to_string('pdf_clientlist.html',
                            {'clients': client})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=client_list.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        # update
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.updated_date = timezone.now()
            client.save()
            #            project = Project.objects.filter(created_date__lte=timezone.now())
            client = Client.objects.all()
            return render(request, 'client_list.html',
                          {'clients': client})
    else:
        # edit
        form = ClientForm(instance=client)
    return render(request, 'client_edit.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')


# Employee
@login_required
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.created_date = timezone.now()
            employee.save()
            employee = Employee.objects.all
            return render(request, 'employee_list.html',
                          {'employees': employee})
    else:
        form = EmployeeForm()
        # print("Else")
    return render(request, 'employee_new.html', {'form': form})


@login_required
def employee_list(request):
    #    project = Project.objects.filter(created_date__lte=timezone.now())
    employee = Employee.objects.all()
    return render(request, 'employee_list.html',
                  {'employees': employee})


@login_required
def employeelist_pdf(request):
    employee = Employee.objects.all()
    html = render_to_string('pdf_employeelist.html',
                            {'employees': employee})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=employee_list.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@login_required
def employeelist_pdf_mail(request):
    employee = Employee.objects.all()
    # construct email
    employee_name = request.POST.get("employee_name")
    subject = 'AK Infotech: Your new Project Assignment!'
    message = f'You have a new Project Assignment Created. Please contact your project Manager for ' \
              f'further details'
    email = EmailMessage(subject,
                         message,
                         settings.EMAIL_HOST_USER,
                         [CustomUser.email])
    html = render_to_string('pdf_employeelist.html', {'employees': employee})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'employee_list.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'employee_list.html',
                  {'employees': employee})


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        # update
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.updated_date = timezone.now()
            employee.save()
            employee = Employee.objects.all()
            return render(request, 'employee_list.html',
                          {'employees': employee})
    else:
        # edit
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form})


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')


@login_required
def employee_assignment(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    assignment = Assignment.objects.filter(employee_name=pk)
    return render(request, 'employee_assignment.html',
                  {'assignments': assignment, 'employee': employee})


@login_required
def project_summary(request, pk):
    project = get_object_or_404(Project, pk=pk)
    assignment = Assignment.objects.filter(project_name=pk)
#    employee_name = get_object_or_404(Assignment, pk=pk)
#    employee = Employee.objects.filter(employee_name=employee_name)
    return render(request, 'project_summary.html',
                  {'assignments': assignment, 'project': project})


@login_required
def admin_projectsummary_pdf(request, pk):
    project = get_object_or_404(Project, pk=pk)
    assignment = Assignment.objects.filter(project_name=pk)
    employee_name = get_object_or_404(Assignment, pk=pk)
    employee = Employee.objects.filter(employee_name=employee_name)
    html = render_to_string('pdf.html',
                            {'assignments': assignment, 'project': project, 'employee': employee})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={project.project_name}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@login_required
def admin_projectsummary_pdf1(request, pk):
    project = get_object_or_404(Project, pk=pk)
    assignment = Assignment.objects.filter(project_name=pk)
    employee_name = get_object_or_404(Assignment, pk=pk)
    employee = Employee.objects.filter(employee_name=employee_name)
    html = render_to_string('pdf.html',
                            {'assignments': assignment, 'project': project, 'employee': employee})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={project.project_name}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + 'css/pdf.css')])
    return response


def projectsummary_pdf1(obj, pk):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('admin_projectsummary_pdf1', pk, args=[obj.id])))


projectsummary_pdf1.short_description = 'ProjectSummary'


@login_required
def admin_projectlist_pdf(request):
    project = Project.objects.all()
    html = render_to_string('pdf_projectlist.html',
                            {'projects': project})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=project_list.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + 'css/pdf.css')])
    return response
