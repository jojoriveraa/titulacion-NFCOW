# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 10:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_customerprofiles_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerProfiles',
            new_name='CustomerProfile',
        ),
    ]
