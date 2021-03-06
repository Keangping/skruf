# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_stoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brudgom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mansjettknapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skjorte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Slips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sløyfe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Smoking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_description', models.CharField(max_length=50)),
                ('product_content', models.TextField(max_length=5000)),
                ('product_type', models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20)),
                ('product_image', models.FileField(upload_to='')),
                ('product_gallery_content', models.TextField(max_length=150)),
                ('product_keyword', models.CharField(max_length=50)),
                ('product_color', models.CharField(choices=[('blå', 'blå'), ('grå', 'grå'), ('sort', 'sort'), ('ivory', 'ivory'), ('hvit', 'hvit'), ('brun', 'brun'), ('lilla', 'lilla'), ('rosa', 'rosa'), ('beige', 'beige'), ('grønn', 'grønn'), ('gul', 'gul'), ('rød', 'rød')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='collection',
            name='type_of_collection',
            field=models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dress',
            name='product_type',
            field=models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stoff',
            name='product_type',
            field=models.CharField(choices=[('dress', 'dress'), ('stoff', 'stoff'), ('brudgom', 'brudgom'), ('skjorte', 'skjorte'), ('sko', 'sko'), ('smoking', 'smoking'), ('slips', 'slips'), ('sløyfe', 'sløyfe'), ('mansjettknapper', 'mansjettknapper')], max_length=20),
        ),
    ]
