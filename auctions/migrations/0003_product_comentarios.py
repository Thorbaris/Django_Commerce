# Generated by Django 3.1.1 on 2020-10-04 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_product_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comentarios',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comments'),
        ),
    ]
