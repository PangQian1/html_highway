# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0007_enweight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardaycount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=5)),
                ('date', models.CharField(max_length=20)),
                ('car1', models.IntegerField()),
                ('car2', models.IntegerField()),
                ('car3', models.IntegerField()),
                ('car4', models.IntegerField()),
            ],
        ),
    ]
