# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0034_delete_od'),
    ]

    operations = [
        migrations.CreateModel(
            name='OD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('province', models.CharField(max_length=20)),
                ('enstation', models.CharField(max_length=50)),
                ('enlon', models.FloatField()),
                ('enlat', models.FloatField()),
                ('exstation', models.CharField(max_length=50)),
                ('exlon', models.FloatField()),
                ('exlat', models.FloatField()),
                ('tp', models.CharField(max_length=20)),
                ('count', models.BigIntegerField(default=0)),
            ],
        ),
    ]
