# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rel_products_orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rel_product_order',
            old_name='id_order',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='rel_product_order',
            old_name='id_product',
            new_name='product',
        ),
    ]
