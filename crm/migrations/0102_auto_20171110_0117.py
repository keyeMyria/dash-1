# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0101_auto_20171107_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(choices=[('餐饮', '餐饮'), ('服务业', '服务业'), ('广告', '广告'), ('兼服务业', '兼服务业'), ('建筑', '建筑'), ('零售业', '零售业'), ('贸易', '贸易'), ('租赁业', '租赁业'), ('制造业', '制造业'), ('娱乐', '娱乐'), ('其它', '其它')], default='汽配', max_length=50, verbose_name='所属行业'),
        ),
    ]
