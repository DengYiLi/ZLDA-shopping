# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('goodsNum', models.IntegerField()),
                ('goodsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
        ),
    ]