# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rel_products_orders', '0003_remove_rel_product_order_price_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rel_product_order',
            name='quantity',
        ),
    ]