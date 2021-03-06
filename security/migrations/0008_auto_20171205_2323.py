# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(
                default='', max_length=100, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(
                default='中国', max_length=50, verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.CharField(
                default='', max_length=100, verbose_name='省'),
        ),

    ]
