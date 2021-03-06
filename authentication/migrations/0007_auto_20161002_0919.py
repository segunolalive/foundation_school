# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 08:19
from __future__ import unicode_literals

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20160930_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=authentication.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
