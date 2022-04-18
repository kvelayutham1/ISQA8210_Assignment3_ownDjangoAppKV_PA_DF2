from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
import weasyprint
from .models import *
from .models import Employee, Client, Project
from .forms import *
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from io import BytesIO
from django.core.mail import EmailMessage

# Create your views here.

now = timezone.now()


# Employee
@login_required
def assignment_new(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            #            assignment.created_date = timezone.now()
            assignment.save()
            assignment = Assignment.objects.all
            email1 = request.POST.get("email")

            # construct email
            employee_name = request.POST.get("employee_name")
            subject = 'AK Infotech: Your new Project Assignment!'
            message = f'You have a new Project Assignment Created. Please contact your project Manager for ' \
                      f'further details'
#            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email1])
            # generate PDF
#            html = render_to_string('pdf_assignment.html', {'assignments': assignment})
#            out = BytesIO()
#            stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
#            weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
            # attach PDF file
#            email.attach(f'{employee_name}.pdf', out.getvalue(), 'application/pdf')
#            email.send()
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email1])
            return render(request, 'assignment_list.html',
                          {'assignments': assignment})
    else:
        form = AssignmentForm()
        # print("Else")
    return render(request, 'assignment_new.html', {'form': form})


@login_required
def assignment_email(request, pk):
    assignment = Assignment.objects.filter(pk=pk)
    email1 = request.POST.get("email")
    subject = 'AK Infotech: Your Project Assignment!'
    message = f'You have a new Project Assignment Created now. Please contact your project Manager for ' \
              f'further details'
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email1])
    html = render_to_string('pdf_assignment.html', {'assignments': assignment})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'pdf_assignment.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'assignment_list.html', {'assignments': assignment})



@login_required
def assignment_list(request):
    assignment = Assignment.objects.all()
    return render(request, 'assignment_list.html',
                  {'assignments': assignment})
    html = render_to_string('pdf_assignment.html',
                            {'assignments': assignment})


@login_required
def assignment_edit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == "POST":
        # update
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.updated_date = timezone.now()
            assignment.save()
            #            project = Project.objects.filter(created_date__lte=timezone.now())
            assignment = Assignment.objects.all()
            return render(request, 'assignment_list.html',
                          {'assignments': assignment})
    else:
        # edit
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignment_edit.html', {'form': form})


@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.delete()
    return redirect('assignment_list')


def projectsummary_pdf1(obj, pk):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('admin_projectsummary_pdf1', pk, args=[obj.id])))
