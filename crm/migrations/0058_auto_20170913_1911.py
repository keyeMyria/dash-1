# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0057_auto_20170913_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='归还日期'),
        ),
    ]
