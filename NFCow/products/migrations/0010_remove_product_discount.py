# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]