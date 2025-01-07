"""MBAZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from application import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('projects/', views.project_list_view, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('experiments/<int:experiment_id>/', views.experiment_detail_view, name='experiment_detail'),
    path('patients/<int:patient_id>/results/', views.patient_results_view, name='patient_results'),
    path('projects/create/', views.project_create_view, name='project_create'),
    path('results/<int:result_id>/', views.project_detail_view, name='result_detail'),
    path('employees/<int:employee_id>/', views.employee_detail_view, name='employee_detail'),
]