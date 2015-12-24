# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('public_name', models.CharField(max_length=255)),
                ('private_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products')),
            ],
        ),
    ]
