# Generated by Django 3.1.1 on 2020-10-13 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20201011_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 0, 56, 54, 651488)),
        ),
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, default=None, to='auctions.product'),
        ),
    ]
