# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 11:36
from __future__ import unicode_literals

import BasicArticle.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicArticle', '0012_auto_20180123_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(null=True, upload_to=BasicArticle.models.get_file_path),
        ),
    ]