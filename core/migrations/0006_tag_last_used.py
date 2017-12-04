# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171204_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='last_used',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
