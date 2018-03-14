# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-13 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='course')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_topics', to='course.Course')),
            ],
        ),
        migrations.AddField(
            model_name='links',
            name='topics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics_links', to='course.Topics'),
        ),
    ]
