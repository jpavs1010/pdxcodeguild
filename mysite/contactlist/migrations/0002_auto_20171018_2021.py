# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contactlist',
            new_name='Contact',
        ),
    ]