from django.contrib import admin

# Register your models here.
from application.models import Employee, Laboratory, Project, Experiments, KeyWords, Protocols, Results, Patient

admin.site.register(Employee)
admin.site.register(Laboratory)
admin.site.register(Project)
admin.site.register(Experiments)
admin.site.register(KeyWords)
admin.site.register(Protocols)
admin.site.register(Results)
admin.site.register(Patient)
