# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfridge', '0003_auto_20170529_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='owner',
            field=models.CharField(default='', max_length=100),
        ),
    ]