# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0030_auto_20181025_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='entrafficvolume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='area',
            name='extrafficvolume',
            field=models.BigIntegerField(default=0),
        ),
    ]