# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-20 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcm', '0002_auto_20170327_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='comment',
            field=models.TextField(default='', verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='eventedition',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.Event', verbose_name='event'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='eventvenue',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='geographicalclassification',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
    ]
