# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0056_auto_20170913_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='接收时间'),
        ),
    ]
