# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0089_auto_20171030_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='has_custom_info',
            field=models.CharField(choices=[('有', '有'), ('无', '无')], default='无', max_length=100, verbose_name='是否有海关信息'),
        ),
    ]
