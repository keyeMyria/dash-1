# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0032_auto_20170817_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ic_status',
            field=models.CharField(choices=[('valid', '有效'), ('invalid', '无效')], default='normal', help_text='经营异常: 已被工商局列入经营异常名录', max_length=10, verbose_name='工商状态'),
        ),
        migrations.AlterField(
            model_name='company',
            name='registered_capital',
            field=models.DecimalField(decimal_places=0, help_text='万元', max_digits=20, verbose_name='注册资金'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('valid', '有效'), ('invalid', '无效')], default='valid', help_text='无效状态，不再为客户提供服务', max_length=10, verbose_name='状态'),
        ),
    ]
