# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import qna.models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='lat',
            field=models.CharField(default='33', max_length=30, validators=[qna.models.lnglat_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='lng',
            field=models.CharField(default='44', max_length=30, validators=[qna.models.lnglat_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='location',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('o', 'Open'), ('p', 'Pending'), ('c', 'Close')], default='o', max_length=1),
        ),
    ]
