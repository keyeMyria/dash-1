# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20171204_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('owner', '创建人'), ('follower', '关注者'), ('member', '成员')], default='member', max_length=50),
        ),
    ]
