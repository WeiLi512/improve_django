# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-08-29 08:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160406_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 29, 8, 16, 15, 866641, tzinfo=utc)),
            preserve_default=False,
        ),
    ]