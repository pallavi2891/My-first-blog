# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallaviBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=20)),
                ('specialized_in', models.CharField(max_length=200)),
            ],
        ),
    ]
