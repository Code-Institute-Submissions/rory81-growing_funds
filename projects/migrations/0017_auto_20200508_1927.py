# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20200502_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Charity', 'Charity'), ('Film', 'Film'), ('Food', 'Food'), ('Games', 'Games'), ('Music', 'Music'), ('Publishing', 'Publishing'), ('Technology', 'Technology')], max_length=10),
        ),
    ]
