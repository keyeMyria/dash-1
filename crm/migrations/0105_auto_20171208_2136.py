# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0104_auto_20171208_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='local_tax_office',
        ),
        migrations.RemoveField(
            model_name='company',
            name='national_tax_office',
        ),
    ]
