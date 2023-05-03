# Generated by Django 2.0.6 on 2021-09-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptobitsapp', '0016_auto_20210831_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedCoins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('minimum_withdraw', models.DecimalField(decimal_places=2, max_digits=35)),
                ('maximum_investment', models.DecimalField(decimal_places=2, max_digits=35)),
                ('maximum_withdraw', models.DecimalField(decimal_places=2, max_digits=35)),
                ('minimum_investment', models.DecimalField(decimal_places=2, max_digits=35)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=35)),
            ],
        ),
    ]
