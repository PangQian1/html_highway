# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-04 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0047_auto_20181104_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='trafficdiff',
        ),
    ]
