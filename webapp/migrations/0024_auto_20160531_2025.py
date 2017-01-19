# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_searchterm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchterm',
            name='category',
            field=models.CharField(choices=[('all', 'all'), ('Hardware and OS', 'Hardware and OS'), ('Desktops', 'Desktops'), ('Tablets', 'Tablets'), ('Phones', 'Phones'), ('Wearables', 'Wearables'), ('Windows', 'Windows'), ('Mac OS X', 'Mac OS X'), ('Linux and Unix', 'Linux and Unix'), ('Programming and Computer Science', 'Programming and Computer Science'), ('Software Development', 'Software Development'), ('Web Development (Front)', 'Web Development (Front)'), ('Web Development (Back)', 'Web Development (Back)'), ('Mobile Development', 'Mobile Development'), ('Game Development', 'Game Development'), ('Algorithms and Data Structures', 'Algorithms and Data Structures'), ('Databases', 'Databases'), ('IDE / Text Editors', 'IDE / Text Editors'), ('Community Discussion', 'Community Discussion'), ('Tutorial', 'Tutorial'), ('Opinion', 'Opinion'), ('Miscellaneous', 'Miscellaneous')], max_length=200),
        ),
    ]
