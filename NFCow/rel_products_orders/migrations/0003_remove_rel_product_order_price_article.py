# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 00:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rel_products_orders', '0002_auto_20151230_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rel_product_order',
            name='price_article',
        ),
    ]
