# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20161207_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(null=True, verbose_name='user weight in kg'),
        ),
    ]