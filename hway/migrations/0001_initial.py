# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-11 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daycount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=5)),
                ('date', models.CharField(max_length=20)),
                ('etc', models.IntegerField()),
                ('mtc', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
