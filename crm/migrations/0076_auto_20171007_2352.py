# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0075_auto_20171007_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareholder',
            name='people_name',
        ),
        migrations.AddField(
            model_name='shareholder',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='shareholder',
            name='sfz',
            field=models.CharField(blank=True, max_length=255, verbose_name='身份证'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='phone',
            field=models.CharField(blank=True, max_length=200, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='role',
            field=models.CharField(choices=[('法人', '法人'), ('股东', '股东'), ('员工', '员工')], default='股东', max_length=10, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='share',
            field=models.FloatField(default=0.1, verbose_name='股份占比'),
        ),
    ]
