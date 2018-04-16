# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-14 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0112_auto_20180329_2333'),
        ('borrow', '0002_auto_20180331_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevertList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, verbose_name='编号')),
                ('revert_borrow_date', models.DateField(verbose_name='归还时间')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Company', verbose_name='所属公司')),
            ],
        ),
        migrations.AlterField(
            model_name='entitylist',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='borrow.RevertList', verbose_name='归还单编号'),
        ),
    ]
