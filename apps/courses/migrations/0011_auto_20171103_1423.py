# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-03 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20171103_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u89c6\u9891\u540d'),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=300, verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]
