# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy_bday', '0002_patient_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default='test@test.com', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(default='555-555-5555', max_length=20),
            preserve_default=False,
        ),
    ]
