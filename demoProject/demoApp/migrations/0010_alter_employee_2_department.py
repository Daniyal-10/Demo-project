# Generated by Django 5.1.2 on 2024-10-25 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0009_employee_2_delete_employeev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_2',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoApp.department'),
        ),
    ]