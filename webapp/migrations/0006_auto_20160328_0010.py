# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_registrationsignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'invalid': 'Enter a valid value', 'required': ''}, max_length=18, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='RegistrationSignUp',
        ),
    ]
