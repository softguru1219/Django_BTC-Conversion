# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-03 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='code',
            field=models.CharField(help_text=' code of crypto currency', max_length=4, unique=True),
        ),
    ]