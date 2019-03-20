# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0057_chargebytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chargebytype_avg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('vtype', models.IntegerField()),
                ('weightfee', models.FloatField()),
                ('feelow', models.FloatField()),
                ('feehigh', models.FloatField()),
                ('low_change_rate', models.FloatField()),
                ('high_change_rate', models.FloatField()),
            ],
        ),
    ]
