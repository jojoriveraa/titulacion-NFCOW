# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_carts', '0002_shopping_cart_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='user',
        ),
    ]
