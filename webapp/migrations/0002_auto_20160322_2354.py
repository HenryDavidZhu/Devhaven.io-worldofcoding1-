# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUp',
            new_name='NewsletterSignUp',
        ),
    ]
