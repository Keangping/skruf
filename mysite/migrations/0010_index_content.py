# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_content', models.TextField(max_length=10000)),
            ],
        ),
    ]
