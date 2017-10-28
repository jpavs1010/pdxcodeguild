# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2)),
                ('county', models.CharField(max_length=20)),
                ('pct_access', models.IntegerField()),
                ('county_id', models.IntegerField()),
            ],
        ),
    ]
