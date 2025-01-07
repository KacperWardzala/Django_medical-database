# Generated by Django 4.1 on 2024-04-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_employee_laboratory_remove_employee_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.employee'),
        ),
        migrations.AddField(
            model_name='project',
            name='projects',
            field=models.ManyToManyField(blank=True, to='application.project'),
        ),
        migrations.CreateModel(
            name='Employes_has_experiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employes_has_experiments', models.CharField(max_length=45)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.employee')),
            ],
        ),
    ]
