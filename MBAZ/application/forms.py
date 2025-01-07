from django import forms
from .models import Project, Employee

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_of_the_project', 'description', 'start_date', 'end_date']


class AddEmployeeForm(forms.Form):
    employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
