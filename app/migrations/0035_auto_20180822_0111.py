# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-22 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='calendarinfo',
            field=models.CharField(max_length=100, verbose_name='Calendar Information'),
        ),
    ]