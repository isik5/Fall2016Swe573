# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caloriewatcher', '0003_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('i', 'i'), ('o', 'o')], max_length=1)),
                ('label', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=20)),
                ('quantity', models.FloatField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caloriewatcher.Entry')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='extra',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='measure',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='what',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='when',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='extra',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='food',
            name='measure',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='what',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='when',
            field=models.DateTimeField(null=True),
        ),
    ]
