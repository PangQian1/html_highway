# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0038_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='number',
            field=models.CharField(default='11', max_length=5),
        ),
    ]
