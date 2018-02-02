# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180202_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='product_content',
            field=models.TextField(default='this is content', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_description',
            field=models.CharField(default='this is dri', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_gallery_content',
            field=models.TextField(default='heel', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_image',
            field=models.FileField(default='djdj', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_keyword',
            field=models.CharField(default='hdhd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='product_type',
            field=models.CharField(choices=[('dress', 'dress'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('mansjettknapper', 'mansjettknapper'), ('sløyfe', 'sløyfe')], default='tyep', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='type_of_collection',
            field=models.CharField(choices=[('dress', 'dress'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('mansjettknapper', 'mansjettknapper'), ('sløyfe', 'sløyfe')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dress',
            name='product_color',
            field=models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20),
        ),
    ]