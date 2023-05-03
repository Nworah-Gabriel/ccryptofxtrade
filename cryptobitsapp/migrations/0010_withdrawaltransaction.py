# Generated by Django 2.0.6 on 2021-08-31 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptobitsapp', '0009_auto_20210831_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=35)),
                ('currency', models.CharField(choices=[('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('BNB', 'bnb'), ('DGE', 'dge'), ('XRP', 'xrp'), ('BCH', 'bch')], default='BTC', max_length=3)),
                ('status', models.CharField(choices=[('SUB', 'submitted'), ('APV', 'approved')], default='SUB', max_length=3)),
                ('address', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
