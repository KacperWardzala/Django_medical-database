# Generated by Django 4.1 on 2024-04-25 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_remove_laboratory_employee_employee_laboratory'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.employee'),
        ),
    ]
