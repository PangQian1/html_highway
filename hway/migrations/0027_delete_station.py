# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0026_delete_area'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Station',
        ),
    ]
