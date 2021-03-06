# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurant_categories'),
        ('products_catalogue', '0002_product_catalogue_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_catalogue',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
    ]
