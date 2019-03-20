# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0012_auto_20181017_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('enweight', models.BigIntegerField()),
                ('exweight', models.BigIntegerField()),
                ('trafficvolume', models.BigIntegerField()),
            ],
        ),
    ]
