# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_profile_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconf',
            name='enable_wechat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='siteconf',
            name='wx_appid',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='siteconf',
            name='wx_appsecret',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
