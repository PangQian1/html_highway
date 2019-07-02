# Generated by Django 2.1.7 on 2019-07-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0071_auto_20190319_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelCoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enSta_id', models.CharField(max_length=20)),
                ('exSta_id', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('vehType', models.IntegerField()),
                ('txl', models.BigIntegerField(default=0)),
                ('travelCoe', models.FloatField()),
            ],
        ),
    ]