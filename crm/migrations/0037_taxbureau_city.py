# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_auto_20170830_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxbureau',
            name='city',
            field=models.CharField(blank=True, choices=[('guangzhou', '广州市'), ('zhuhai', '珠海市'), ('foshan', '佛山市')], default='guangzhou', max_length=200, verbose_name='市'),
        ),
    ]
