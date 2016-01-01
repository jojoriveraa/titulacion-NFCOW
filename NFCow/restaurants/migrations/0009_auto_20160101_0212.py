# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurant_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='restaurants_category', to='categories.Category'),
        ),
    ]