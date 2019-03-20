# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0051_auto_20181122_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('province', models.CharField(max_length=20)),
                ('cycle', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]