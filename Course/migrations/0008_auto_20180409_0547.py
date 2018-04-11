# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 05:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course', '0007_links_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_createdby', to=settings.AUTH_USER_MODEL),
        ),
    ]
