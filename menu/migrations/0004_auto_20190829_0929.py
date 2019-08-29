# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-08-29 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20190829_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='expiration_date',
            new_name='expiration_datetime',
        ),
        migrations.AddField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
