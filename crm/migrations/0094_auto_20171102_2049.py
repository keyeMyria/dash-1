# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0093_auto_20171102_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='legal_people_phone',
            new_name='legal_phone',
        ),
    ]
