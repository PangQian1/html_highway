# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0005_auto_20181012_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinceheavycount',
            name='heavy',
            field=models.BigIntegerField(),
        ),
    ]
