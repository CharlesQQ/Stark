# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-26 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arya', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='os_type',
            field=models.CharField(choices=[('redhat', 'Redhat\\Centos'), ('ubuntu', 'Ubuntu'), ('suse', 'Suse'), ('windows', 'Windows')], default='redhat', max_length=64),
        ),
    ]
