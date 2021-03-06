# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('malls', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('mall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malls.Mall')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
    ]
