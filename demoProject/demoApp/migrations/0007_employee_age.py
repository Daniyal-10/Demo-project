# Generated by Django 5.1.2 on 2024-10-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0006_alter_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
