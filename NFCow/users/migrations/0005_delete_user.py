# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151229_0756'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
