# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-10 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='female', max_length=6, verbose_name='\u6027\u522b'),
        ),
    ]