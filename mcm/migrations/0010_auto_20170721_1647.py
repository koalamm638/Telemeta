# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-21 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcm', '0009_auto_20170721_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='text',
            field=models.TextField(default='', verbose_name='text'),
        ),
    ]