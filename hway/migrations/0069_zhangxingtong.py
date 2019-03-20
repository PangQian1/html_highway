# Generated by Django 2.1.7 on 2019-03-19 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hway', '0068_delete_chongqing_od'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhangXingTong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=50)),
                ('longi', models.FloatField()),
                ('lati', models.FloatField()),
            ],
        ),
    ]