# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-28 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0010_auto_20171206_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileold',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfileOld',
        ),
    ]