# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0031_auto_20181025_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='engreentrafficvolume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='area',
            name='exgreentrafficvolume',
            field=models.BigIntegerField(default=0),
        ),
    ]
