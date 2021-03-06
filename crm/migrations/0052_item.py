# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0051_auto_20170912_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_title', models.CharField(blank=True, editable=False, max_length=255)),
                ('item', models.CharField(blank=True, choices=[('身份证原件', '身份证原件'), ('营业执照', '营业执照'), ('其它', '其它')], max_length=200, verbose_name='物品')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('status', models.CharField(blank=True, choices=[('寄存', '寄存'), ('借出', '借出'), ('已归还', '已归还'), ('遗失', '遗失')], max_length=200, verbose_name='状态')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='归还日期')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建于')),
                ('status_updated', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, verbose_name='备注')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='借出人')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Company', verbose_name='公司')),
            ],
        ),
    ]
