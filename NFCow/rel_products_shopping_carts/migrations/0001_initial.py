# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_carts', '0001_initial'),
        ('products', '0009_remove_product_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rel_Product_Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_carts.Shopping_Cart')),
            ],
        ),
    ]