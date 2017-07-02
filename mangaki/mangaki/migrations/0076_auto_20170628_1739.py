# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0075_merge_20170623_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extlanguage',
            name='ext_lang',
            field=models.CharField(db_index=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='worktitle',
            name='type',
            field=models.CharField(blank=True, choices=[('main', 'principal'), ('official', 'officiel'), ('synonym', 'synonyme'), ('short', 'court')], db_index=True, max_length=9),
        ),
    ]
