# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0087_auto_20171015_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='rating',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10, verbose_name='评级'),
        ),
    ]