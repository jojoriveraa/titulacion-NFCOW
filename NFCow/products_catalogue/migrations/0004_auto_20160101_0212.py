# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products_catalogue', '0003_product_catalogue_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_catalogue',
            name='category',
        ),
        migrations.AddField(
            model_name='product_catalogue',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products_category', to='categories.Category'),
        ),
    ]
