# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-19 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20181019_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Publication Authors'),
        ),
        migrations.AddField(
            model_name='publication',
            name='conference',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Publication Conference'),
        ),
    ]
