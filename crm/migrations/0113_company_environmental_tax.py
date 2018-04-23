# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-21 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0112_auto_20180329_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='environmental_tax',
            field=models.CharField(blank=True, choices=[('有', '有'), ('无', '无')], max_length=100, verbose_name='环保税'),
        ),
    ]
