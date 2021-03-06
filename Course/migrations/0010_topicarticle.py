# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasicArticle', '0013_auto_20180227_1136'),
        ('Course', '0009_auto_20180409_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics_articles', to='BasicArticle.Articles')),
                ('topics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics_articles', to='Course.Topics')),
            ],
        ),
    ]
