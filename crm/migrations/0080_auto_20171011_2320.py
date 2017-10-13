# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0079_auto_20171011_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='received_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='签收日期'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]