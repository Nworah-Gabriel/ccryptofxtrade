# Generated by Django 2.0.6 on 2021-09-02 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptobitsapp', '0027_remove_withdrawaltransaction_currency_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawaltransaction',
            name='coin_code',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='withdrawaltransaction',
            name='currency_coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Accepted_Coin_withdraw', to='cryptobitsapp.AcceptedCoin'),
        ),
    ]
