# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_carts', '0001_initial'),
        ('orders', '0005_auto_20160101_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='shopping_cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopping_carts.Shopping_Cart'),
            preserve_default=False,
        ),
    ]
