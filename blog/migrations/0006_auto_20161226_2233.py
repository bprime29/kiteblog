# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-26 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161226_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Images'),
        ),
    ]