from django.http import HttpResponse
from application.models import Employee, Project, Experiments, ExperimentParticipant, Results, Patient, Employee
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Employee
from .forms import AddEmployeeForm
from django.shortcuts import render, redirect

# Existing imports...

def welcome_view(request):
    return render(request, 'welcome.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/projects/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/projects/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Existing views...
'''
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/projects/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
'''
@login_required
def project_list_view(request):
    projects = Project.objects.all()
    return render(request, "project_list.html", {'projects': projects})

@login_required
def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    experiments = project.experiments.all()
    employees = project.employee_set.all()
    form = AddEmployeeForm()

    if request.method == 'POST':
        if 'add_employee' in request.POST:
            form = AddEmployeeForm(request.POST)
            if form.is_valid():
                selected_employees = form.cleaned_data['employees']
                project.employee_set.add(*selected_employees)
                return redirect('project_detail', project_id=project.id)

        elif 'delete_employee' in request.POST:
            employee_ids = request.POST.getlist('employee_ids')
            if employee_ids:
                employees_to_remove = Employee.objects.filter(id__in=employee_ids)
                project.employee_set.remove(*employees_to_remove)
                return redirect('project_detail', project_id=project.id)

    return render(request, 'project_detail.html', {
        'project': project,
        'experiments': experiments,
        'employees': employees,
        'form': form,
    })


@login_required
def experiment_detail_view(request, experiment_id):
    experiment = get_object_or_404(Experiments, id=experiment_id)
    results = Results.objects.filter(Experiments=experiment)
    return render(request, "experiment_detail.html", {
        'experiment': experiment,
        'results': results
    })

@login_required
def patient_results_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    results = patient.results.all()
    return render(request, 'patient_results.html', {'patient': patient, 'results': results})

@login_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def employee_detail_view(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "employee_detail.html", {'employee': employee})
