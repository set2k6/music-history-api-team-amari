# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hannah', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(to='hannah.Album'),
        ),
    ]
