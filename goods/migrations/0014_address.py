# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_auto_20170624_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=10)),
                ('userName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('detailAddress', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('ems', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
