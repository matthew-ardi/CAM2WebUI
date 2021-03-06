# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170606_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentmemberimg', models.CharField(max_length=300)),
                ('currentmembername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('event', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderimg', models.CharField(max_length=300)),
                ('leadertitle', models.CharField(max_length=50)),
                ('leadername', models.CharField(max_length=50)),
                ('leaderpagelink', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OldMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldmembername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperinfo', models.CharField(max_length=500)),
                ('paperlink', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamimg', models.CharField(max_length=300)),
            ],
        ),
    ]
