# Generated by Django 3.2.7 on 2021-09-07 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptobitsapp', '0037_remove_userbasicinformation_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbasicinformation',
            old_name='birth_date',
            new_name='date_of_birth',
        ),
    ]
