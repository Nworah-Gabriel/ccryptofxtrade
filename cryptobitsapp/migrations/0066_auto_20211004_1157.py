# Generated by Django 3.2.7 on 2021-10-04 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cryptobitsapp', '0065_auto_20211004_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdefistaking',
            name='farm_quantity',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=35),
        ),
        migrations.AlterField(
            model_name='userdefistaking',
            name='interest_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 66442, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userdefistaking',
            name='last_credit_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 65444, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userdefistaking',
            name='stake_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 65444, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userstockstaking',
            name='interest_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 64445, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userstockstaking',
            name='last_credit_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 64445, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userstockstaking',
            name='stake_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 10, 57, 19, 64445, tzinfo=utc), null=True),
        ),
    ]
