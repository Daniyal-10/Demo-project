# Generated by Django 5.1.2 on 2024-10-24 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0007_employee_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deparment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employeev',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(blank=True, max_length=25, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demoApp.department'),
        ),
    ]
