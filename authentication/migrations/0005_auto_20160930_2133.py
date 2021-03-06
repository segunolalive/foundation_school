# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20160930_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='church',
            field=models.CharField(blank=True, default='not set', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, default='not set', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zone',
            field=models.CharField(blank=True, default='not set', max_length=40, null=True),
        ),
    ]
