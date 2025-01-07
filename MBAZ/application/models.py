from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=45)
    sec_name = models.CharField(max_length=45)
    pesel = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    Laboratory = models.ForeignKey('Laboratory', on_delete=models.CASCADE, null=True)
    Projects = models.ManyToManyField('Project', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.sec_name}"


class Laboratory(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

class Project(models.Model):
    name_of_the_project = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()

class Experiments(models.Model):
    Name_of_experiment = models.CharField(max_length=45)
    Start_date = models.DateField()
    End_date = models.DateField()
    Status = models.CharField(max_length=45)
    Description_of_results = models.CharField(max_length=45)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='experiments', null=True)


class ExperimentParticipant(models.Model):
    experiment = models.ForeignKey('Experiments', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True)

class KeyWords(models.Model):
    key_word = models.CharField(max_length=45)
    Project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
    Experiments = models.ForeignKey('Experiments', on_delete=models.CASCADE, null=True)

class Protocols(models.Model):
    protocol_name = models.CharField(max_length=45)
    Experiments = models.ForeignKey('Experiments', on_delete=models.CASCADE, null=True)

class Results(models.Model):
    filename = models.CharField(max_length=45)
    Experiments = models.ForeignKey('Experiments', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.filename
class Patient(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    sex = models.CharField(max_length=1)  # Assuming 'M' or 'F'
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=45)
    results = models.ManyToManyField('Results', blank=True)
