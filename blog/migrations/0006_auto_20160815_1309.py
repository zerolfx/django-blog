# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160815_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='main',
            new_name='body',
        ),
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='111', max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
    ]
