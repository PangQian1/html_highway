# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0041_auto_20181030_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('province', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('enstation', models.CharField(max_length=50)),
                ('exstation', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
