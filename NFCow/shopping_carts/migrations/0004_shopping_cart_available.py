# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_carts', '0003_remove_shopping_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='available',
            field=models.NullBooleanField(),
        ),
    ]
