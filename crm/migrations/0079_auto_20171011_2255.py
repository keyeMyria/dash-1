# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 14:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0078_auto_20171009_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('action', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('items', jsonfield.fields.JSONField(default=[], editable=False, verbose_name='物品列表')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作员')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemborrowingrecord',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='itemborrowingrecord',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemborrowingrecord',
            name='lender',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.RemoveField(
            model_name='item',
            name='company_title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='物品名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('营业执照正本', '营业执照正本'), ('营业执照副本', '营业执照副本'), ('金税盘', '金税盘'), ('发票领购本', '发票领购本'), ('公章', '公章'), ('发票章', '发票章'), ('财务章', '财务章'), ('私章', '私章'), ('公司章程', '公司章程'), ('扣款协议', '扣款协议'), ('开户许可证', '开户许可证'), ('机构信用代码证', '机构信用代码证'), ('身份证原件', '身份证原件'), ('开业通知书', '开业通知书'), ('变更通知书', '变更通知书'), ('账册', '账册'), ('凭证', '凭证'), ('租赁合同', '租赁合同'), ('汇缴报告', '汇缴报告'), ('其它', '其它')], default='身份证原件', max_length=100, verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to=settings.AUTH_USER_MODEL, verbose_name='借用人'),
        ),
        migrations.AlterField(
            model_name='item',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Company', verbose_name='所属客户'),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('寄存', '寄存'), ('借出', '借出'), ('已归还', '已归还'), ('遗失', '遗失'), ('损坏', '损坏')], default='寄存', max_length=50, verbose_name='状态'),
        ),
        migrations.DeleteModel(
            name='ItemBorrowingRecord',
        ),
        migrations.AddField(
            model_name='log',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Item'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
