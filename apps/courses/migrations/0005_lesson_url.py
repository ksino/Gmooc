# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-30 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.CharField(default='', max_length=100, verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]
