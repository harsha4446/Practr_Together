# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170328_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, height_field=245, null=True, upload_to=users.models.upload_loction, width_field=220),
        ),
    ]
