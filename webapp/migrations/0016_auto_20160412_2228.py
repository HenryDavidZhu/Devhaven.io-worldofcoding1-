# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20160412_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]