# Generated by Django 4.2.1 on 2023-09-03 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zidcode',
            new_name='contact_no',
        ),
    ]