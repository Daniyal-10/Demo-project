# Generated by Django 5.1.2 on 2024-10-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0005_alter_employee_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
