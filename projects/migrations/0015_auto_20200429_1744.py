# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 15:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20200429_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
