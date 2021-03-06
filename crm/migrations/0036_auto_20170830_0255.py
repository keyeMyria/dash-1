# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0035_company_legal_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxbureau',
            name='full_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='全称'),
        ),
        migrations.AlterField(
            model_name='taxbureau',
            name='district',
            field=models.CharField(blank=True, choices=[('baiyun', '白云区'), ('tianhe', '天河区'), ('panyu', '番禺区'), ('yuexiu', '越秀区'), ('haizhu', '海珠区'), ('zengcheng', '增城区'), ('nansha', '南沙区'), ('conghua', '从化区'), ('liwan', '荔湾区'), ('huadu', '花都区'), ('huangpu', '黄埔区'), ('luogang', '萝岗区'), ('huadu', '花都区'), ('develop', '开发区'), ('xiangzhou', '香洲区'), ('other', '其它地区')], max_length=50, verbose_name='所属区'),
        ),
    ]
