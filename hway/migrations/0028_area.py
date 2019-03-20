# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0027_delete_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('province', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('stationname', models.CharField(max_length=50)),
                ('enweight', models.IntegerField(default=0)),
                ('exweight', models.IntegerField(default=0)),
                ('entrafficvolume', models.IntegerField(default=0)),
                ('extrafficvolume', models.IntegerField(default=0)),
                ('engreentrafficvolume', models.IntegerField(default=0)),
                ('exgreentrafficvolume', models.IntegerField(default=0)),
                ('fee', models.BigIntegerField(default=0)),
            ],
        ),
    ]