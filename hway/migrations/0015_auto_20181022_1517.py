# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0014_auto_20181019_1605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Provinceheavycount',
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]
