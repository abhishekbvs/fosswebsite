# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20171130_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumniinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
