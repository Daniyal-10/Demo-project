# Generated by Django 5.1.2 on 2024-10-25 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0013_rename_name_customer_first_name_customer_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='id',
            new_name='customer_id',
        ),
    ]
