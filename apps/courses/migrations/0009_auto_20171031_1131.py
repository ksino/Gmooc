# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-31 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='need_know',
            field=models.CharField(default='', max_length=300, verbose_name='\u8bfe\u7a0b\u9700\u77e5'),
        ),
        migrations.AddField(
            model_name='course',
            name='tell_you',
            field=models.CharField(default='', max_length=300, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60'),
        ),
    ]
