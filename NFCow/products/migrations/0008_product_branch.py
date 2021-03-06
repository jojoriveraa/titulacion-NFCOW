# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0003_merge'),
        ('products', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch',
            field=models.ManyToManyField(blank=True, related_name='products_in_branch', to='branches.Branch'),
        ),
    ]
