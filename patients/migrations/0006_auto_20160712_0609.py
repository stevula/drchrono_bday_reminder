# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20160712_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expires_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
