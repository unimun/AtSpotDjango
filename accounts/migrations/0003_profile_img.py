# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-08 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170909_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
