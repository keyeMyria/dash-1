# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_accesstoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesstoken',
            name='scope',
            field=models.CharField(default='snsapi_userinfo', max_length=200),
        ),
    ]
