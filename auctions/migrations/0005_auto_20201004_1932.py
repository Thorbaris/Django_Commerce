# Generated by Django 3.1.1 on 2020-10-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201004_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(default='', max_length=256),
        ),
    ]
