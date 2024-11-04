# Generated by Django 5.1.2 on 2024-10-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
                ('salary', models.IntegerField(verbose_name=10)),
            ],
        ),
    ]